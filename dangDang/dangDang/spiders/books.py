import scrapy
from ..items import DangdangItem
from scrapy.http.request import Request


class BooksSpider(scrapy.Spider):
    '''爬取当当网图书信息'''
    name = 'books'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://bang.dangdang.com/books/newhotsales/01.00.00.00.00.00-24hours-0-0-1-1']
    i = 1  # 添加序号

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)

        self.num = kwargs.get('num')
        self.url = kwargs.get('url')

    def start_requests(self):
        for offset in range(1, int(self.num)+1):
            # 可观测到，每页变化的网站只有最后一个数字
            url = self.url+str(offset)
            yield Request(url, callback=self.parse)  # callback调用parse函数

    def parse(self, response):
        items = []
        subselector = response.xpath('//ul[@class="bang_list clearfix bang_list_mode"]/li')

        # 获取图片路径
        src_list = response.xpath('//ul[@class="bang_list clearfix bang_list_mode"]/li/div[2]/a').css('img::attr(src)').extract()

        for get_info in subselector:
            item = DangdangItem()
            item['number'] = self.i
            item['bookname'] = get_info.xpath('./div[3]/a/text()').extract()
            item['discuss'] = get_info.xpath('./div[4]/a/text()').extract()
            item['recommend'] = get_info.xpath('./div[4]/span[2]/text()').extract()
            item['author'] = get_info.xpath('./div[5]/a/text()').extract()
            item['pubdate'] = get_info.xpath('./div[6]/span/text()').extract()
            item['press'] = get_info.xpath('./div[6]/a/text()').extract()
            item['origin_price'] = get_info.xpath('./div[7]/p/span[2]/text()').extract()
            item['now_price'] = get_info.xpath('./div[7]/p/span[1]/text()').extract()
            items.append(item)
            self.i += 1

        # 获取书名
        title_list = []
        for item in items:
            title_list.append(item['bookname'][0])

        item['image_urls'] = src_list
        item['image_names'] = title_list
        return items
