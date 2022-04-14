import scrapy
from ..items import TodaymovieItem


class WuhanmoviespiderSpider(scrapy.Spider):
    name = 'wuHanMovieSpider'
    allowed_domains = ['2345.com']
    start_urls = ['https://dianying.2345.com/top/hot.html']

    def parse(self, response):
        items = []
        subselector = response.xpath('//div[@class="txt"]')
        for getName in subselector:
            item = TodaymovieItem()
            item['movieName'] = getName.xpath('./p/span/a/text()').extract()
            item['actor'] = getName.xpath('./p[@class="pActor"]/a/text()').extract()
            items.append(item)
        return items
