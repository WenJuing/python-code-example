import pymysql


d = {' ': 5, 'a': 12, 'b': 10, 'c': 8}

d.pop(' ')
print(d)
""" conn = pymysql.connect('localhost', user='root', passwd='123123', db='py_sql')
cursor = conn.cursor()

res = 0
for k, v in d.items():
    sql = "insert into count_kyyy_words values(null," + "'" + k + "'," + "'" + str(v) + "')"
    res += cursor.execute(sql)
print("有%d条被影响" % res)
cursor.close()
conn.commit()
conn.close() """
