# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


class ZhonghengPipeline:
    def process_item(self, item, spider):
        f = open('xiaoshuo_rank.txt', 'a+', encoding='utf8')
        f.write(item['author'][0] + '\n')
        f.close()
        return item
