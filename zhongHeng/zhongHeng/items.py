# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhonghengItem(scrapy.Item):
    book = scrapy.Field()
    author = scrapy.Field()
    label = scrapy.Field()
    acount = scrapy.Field()
