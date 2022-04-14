import pandas as pd
import jieba
import re
import pymysql


with open("./kaoyanYingyuYi05-16.txt", "r", encoding="utf8") as o:
    text = o.read()
    text = re.sub('[\u3000\n\t]', '', text)
words_list = jieba.lcut(text)
# 导入停词
stopwords = open("./en_stopwords.txt", encoding="utf8").read().split()
# 去除边缘空格
for i in stopwords:
    i.strip()
# 设置停词
for i in stopwords:
    while i in words_list:
        words_list.remove(i)
    while i.capitalize() in words_list:
        words_list.remove(i.capitalize())
se = pd.Series(words_list)
countDict = dict(se.value_counts())  # value为频数
countDict.pop(' ')  # 删除值为空的那个

# 将数据存入数据库
conn = pymysql.connect('localhost', user='root', passwd='123123', db='py_sql')
cursor = conn.cursor()

res = 0  # 变量res用来记录被影响的行数
for k, v in countDict.items():
    try:
        sql = "insert into count_kyyy_words values(null," + "'" + k + "'," + "'" + str(v) + "')"
        res += cursor.execute(sql)
    except Exception as e:
        print("插入失败", e)
        conn.rollback()
print("有%d条被影响" % res)
cursor.close()
conn.commit()
conn.close()

print(countDict)
