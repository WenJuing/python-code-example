from scrapy.selector import Selector
import urllib.request

url = 'http://www.dadagodo.com'

html = urllib.request.urlopen(url, timeout=3).read().decode('utf8')
with open('111.html', 'w', encoding='utf-8') as file_o:
    file_o.write(html)
with open('111.html', 'r', encoding='utf-8') as file_o:
    contents = file_o.read()
Selector(text=contents).xpath('/*').extract()
