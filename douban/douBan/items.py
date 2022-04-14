# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()          # 电影名
    actor = scrapy.Field()          # 演员（导演）
    detail = scrapy.Field()         # 电影细节
    rank = scrapy.Field()           # 评分
    ranked_count = scrapy.Field()   # 评分人数
    number = scrapy.Field()         # No.号
    image_urls = scrapy.Field()     # 电影封面地址（image_urls是系统设置好的，不能改动！！）
    image_names = scrapy.Field()    # 图片名字
    # images = scrapy.Field()         # 有关图片的一些信息


class BookItem(scrapy.Item):
    '''豆瓣图书'''
    bookname = scrapy.Field()   # 图书名称
    author = scrapy.Field()     # 作者
    press = scrapy.Field()      # 出版社
    pubdata = scrapy.Field()    # 出版时间
    price = scrapy.Field()      # 价格
    ISBN = scrapy.Field()       # ISBN（详情页）
    picture = scrapy.Field()    # 图片名
    introduction = scrapy.Field()   # 简介（详情页）
    many = scrapy.Field()       # 含有多个数据
