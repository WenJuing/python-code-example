# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import re
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http.request import Request
from scrapy.exceptions import DropItem


class RankPipeline:
    def process_item(self, item, spider):
        # 存储排行榜中的电影信息
        with open("douban_rank.txt", "a+", encoding="utf8") as file:
            title = re.sub('[ /]', '', item['title'][0])
            time = re.sub('[(].*', '', item['detail'][0])
            actor = re.sub('[\\d|-]*', '', item['detail'][0])
            file.write("\n片名：" + title.strip() + "\n")
            file.write("时间：" + time.strip() + "\n")
            file.write("演员：" + actor.strip() + "\n")
            file.write("评分：" + item['rank'][0] + "\n")
            file.write("评分人数：" + item['ranked_count'][0] + "\n")
        return item


class Top250Pipeline:
    def process_item(self, item, spider):
        # 存储top250中的电影信息
        with open("douban_top250.txt", "a+", encoding="utf8") as file:
            director_actor = re.split('主演', item['actor'][0])  # 把导演和演员分开
            director_actor[0] = re.sub(' ', '', director_actor[0])
            director_actor[1] = re.sub(' ', '', director_actor[1])
            item['actor'][1] = re.sub(' ', '', item['actor'][1])
            file.write(
                "-------------------------------------[No. " + str(item['number']) + "]---")
            file.write("\n片名：" + item['title'][0])
            file.write(director_actor[0] + "\n")
            file.write("演员" + director_actor[1] + "\n")
            file.write("年份/国家/类型：" + item['actor'][1].strip() + "\n")
            file.write("评分：" + item['rank'][0] + "\n")
            file.write("评分人数：" + item['ranked_count'][0] + "\n")
        return item


class Top250ImgPipeline(ImagesPipeline):
    # 重写get_media_requests方法是为了获取item
    def get_media_requests(self, item, info):
        # 此时获取到的item是一个列表，需要循环获取每一个url，并将相应的response对象传给file_path
        for url in item["image_urls"]:
            yield Request(url=url, meta={"index": item["image_urls"].index(url), "item": item})

    # 重写file_path方法是为了修改文件名
    def file_path(self, request, response=None, info=None):
        item = request.meta["item"]
        index = request.meta["index"]
        return f'full/{item["image_names"][index]}.jpg'

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Image Downloaded Failed!!!')
        return item


class BookPipeline:
    def process_item(self, item, spider):
        # 存储排行榜中的图书信息
        with open("book.txt", "a+", encoding="utf8") as file:
            bookname = item['bookname']
            info = re.split('/', item['many'][0])
            author = info[0]
            press = info[1]
            pubdate = info[2]
            price = info[3]
            print("--------"+price)
            file.write("\n书名：" + bookname[0] + "\n")
            file.write("作者：" + author + "\n")
            file.write("出版社：" + press + "\n")
            file.write("出版日期：" + pubdate + "\n")
            file.write("价格：" + price + "\n")
        return item
