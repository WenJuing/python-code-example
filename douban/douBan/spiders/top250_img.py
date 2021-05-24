import scrapy
from ..items import DoubanItem


class Top250ImgSpider(scrapy.Spider):
    name = 'top250_img'
    allowed_domains = ['douban.com']
    start_urls = ['http://douban.com/']

    def parse(self, response):
        pass
