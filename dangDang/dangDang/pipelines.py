# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# 商业转载请联系作者获得授权，非商业转载请注明出处。
# For commercial use, please contact the author for authorization. For non-commercial use, please indicate the source.
# 协议(License)：署名-非商业性使用-相同方式共享 4.0 国际 (CC BY-NC-SA 4.0)
# 作者(Author)：炭治文
# 链接(URL)：http://blog.dadagodo.com/index.php/2021/05/30/python-scrapy-%e7%88%ac%e5%8f%96%e8%b1%86%e7%93%a3%e7%bd%91%e7%9a%84%e7%94%b5%e5%bd%b1%e5%9b%be%e7%89%87/
# 来源(Source)：炭治文のblog

from scrapy.pipelines.images import ImagesPipeline
from scrapy.http.request import Request
from scrapy.exceptions import DropItem


class DangdangPipeline(ImagesPipeline):
    def process_item(self, item, spider):
        with open("dangdang_books.txt", "a+", encoding="utf8") as file:
            file.write("--"+str(item['number'])+"-"*10+"\n")
            file.write("图书名称："+item['bookname'][0]+"\n")
            file.write("作者："+item['author'][0]+"\n")
            file.write("出版社："+item['press'][0]+"\n")
            file.write("出版日期："+item['pubdate'][0]+"\n")
            file.write("原价："+item['origin_price'][0]+"\n")
            file.write("现价："+item['now_price'][0]+"\n")
            file.write("评论数："+str(item['discuss'][0])+"\n")
            file.write("推荐度："+item['recommend'][0]+"\n")
        return item

    # 重写get_media_requests方法是为了获取item
    def get_media_requests(self, item, info):
        # 此时获取到的item是一个列表，需要循环获取每一个url，并将相应的response对象传给file_path
        for url in item["image_urls"]:
            yield Request(url=url, meta={"index": item["image_urls"].index(url), "item": item})

    # 重写file_path方法是为了修改文件名
    def file_path(self, request, response=None, info=None):
        item = request.meta["item"]
        index = request.meta["index"]
        return f'dang/{item["image_names"][index]}.jpg'

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Image Downloaded Failed!!!')
        return item
