import scrapy
from ..items import BookItem


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/top250?icn=index-book250-all']

    def parse(self, response):
        items = []
        subselector = response.xpath('//tr[@class="item"]')
        for i in subselector:
            item = BookItem()
            item['bookname'] = i.xpath('./td[2]/div/a/@title').extract()
            # many包含作者/出版社/出版日期/价格
            item['many'] = i.xpath('./td[2]/p[1]/text()').extract()
            items.append(item)

        return items
