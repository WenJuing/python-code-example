import scrapy
from ..items import ZhonghengItem


class RankSpider(scrapy.Spider):
    name = 'rank'
    allowed_domains = ['www.zongheng.com/']
    start_urls = ['http://www.zongheng.com/rank.html']

    def parse(self, response):
        authon_list = response.xpath('//div[@class="rank_i_bname"]')
        items = []

        for get in authon_list:
            item = ZhonghengItem()
            item['author'] = get.xpaht('./a/text()').extract()
            items.append(item)
        return items
