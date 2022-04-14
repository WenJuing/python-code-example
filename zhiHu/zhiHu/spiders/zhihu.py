import scrapy
from scrapy.http.request import Request


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://zhihu.com/']

    def start_requests(self):
        url = 'https://www.zhihu.com/api/v4/members/jing-pin-la-jiao?include=allow_message%2Cis_fo\
            llowed%2Cis_following%2Cis_org%2Cis_blocking%2Cemployments%2Canswer_count%2Cfollower_count%2Carticles_count%2Cgender%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics'
        yield Request(url, callback=self.parse)

    def parse(self, response):
        print(response.text)
