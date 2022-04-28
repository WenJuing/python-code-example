# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    bookname = scrapy.Field()   # 书名
    discuss = scrapy.Field()    # 评论数
    recommend = scrapy.Field()  # 推荐度
    author = scrapy.Field()     # 作者
    pubdate = scrapy.Field()    # 出版日期
    press = scrapy.Field()      # 出版社
    origin_price = scrapy.Field()  # 原价
    now_price = scrapy.Field()     # 现价
    number = scrapy.Field()     # 序号

    image_urls = scrapy.Field()   # 图片路径
    image_names = scrapy.Field()  # 图片名字
