from scrapy import cmdline
# 启动爬虫脚本
# cmdline.execute('scrapy crawl top250'.split())
cmdline.execute('scrapy crawl books -a num=1 -a url=http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-24hours-0-0-1-'.split())
