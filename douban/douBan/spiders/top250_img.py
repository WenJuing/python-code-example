import scrapy
from scrapy.http.request import Request
from ..items import DoubanItem


class Top250ImgSpider(scrapy.Spider):
    name = 'top250_img'
    allowed_domains = ['douban.com']
    start_urls = ['http://douban.com/']

    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield Request(url, callback=self.parse)

    def parse(self, response):
        subselector = response.xpath('//div[@class="info"]')
        items = []
        item = DoubanItem()

        # 获取图片路径，src_list是个列表
        src_list = response.xpath('//div[@class="pic"]').css('a img::attr(src)').extract()

        # 获取电影名称，title_list是个列表
        title_list = []

        for get in subselector:
            item2 = DoubanItem()
            item2['title'] = get.xpath('./div/a/span/text()').extract()
            items.append(item2)

        for item in items:
            title_list.append(item['title'][0])

        # 接受参数必须为列表
        item['image_urls'] = src_list
        item['image_names'] = title_list
        yield item
