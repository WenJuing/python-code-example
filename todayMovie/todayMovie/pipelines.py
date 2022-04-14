# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


class TodaymoviePipeline:
    def process_item(self, item, spider):
        with open("10_hot_books.txt", "a+", encoding="utf8") as file:
            file.write(item['movieName'][0] + "\n")
            file.write("主演：")
            file.write(item['actor'][0] + " ")
            file.write(item['actor'][1] + " ")
            file.write(item['actor'][2] + "\n")
        return item
