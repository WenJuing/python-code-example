import re
import urllib.request


class GetInfo():
    '''爬虫实战'''
    def __init__(self, url):
        self.url = url
        self.html = urllib.request.urlopen(url, timeout=2).read().decode('utf8')

    def clear_label(self):
        '''清除标签'''
        self.html = re.sub('</?.*/?[>"]', "", self.html)

    def clear_blank(self):
        '''清除空行'''
        self.html = re.sub(' ', "", self.html)
        self.html = re.sub('\r\n', "", self.html)

    def clear_other(self):
        '''清除其他'''
        # 清除数字开头，双引号结束
        self.html = re.sub(r'\d.*(=")', "", self.html)
        # 清除双引号开头，>结束
        self.html = re.sub(r'".*>', "", self.html)

    def save_txt(self, filename='default.txt'):
        '''将数据保存到txt文件'''
        with open(filename, 'w+', encoding='utf-8') as file_o:
            file_o.write(self.html)


url = 'https://dianying.2345.com/top/hot.html'
html = GetInfo(url)
# html.clear_label()
# html.clear_blank()
# html.clear_other()
html.save_txt('zhihu.txt')
