from asyncio.windows_events import NULL
import pymysql


class reviseSql():
    def __init__(self, host, user, passwd, db):
        self.host = host
        self.user = user
        self.passed = passwd
        self.db = db
        self.conn = pymysql.connect(host=host, user=user, passwd=passwd, db=db)
        self.conn.select_db(self.db)
        self.cursor = self.conn.cursor()

    def close_all(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

    def insert_one(self, sql):
        res = self.cursor.execute(sql)
        print("插入成功，共有%d行被影响" % res)

    def insert_many(self, table_name, data):
        sql = "insert into " + table_name + " values(%s,%s,%s,%s)"
        res = self.cursor.executemany(sql, data)
        print("插入成功，共有%d行被影响" % res)


admin = reviseSql('localhost', 'root', '123123', 'eshop')
# admin.insert_one("insert into test values(null,'bbbb',18,173.4)")
for i in range(5):
    admin.insert_many('test', [(NULL, 'aabbcc', i+10, 199)])
admin.close_all()
