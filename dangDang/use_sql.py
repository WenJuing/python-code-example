import pymysql


class useSql():
    '''使用数据库'''

    def __init__(self, host, user, passwd, db):
        '''初始化，连接数据库并获取游标'''
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.conn = pymysql.connect(host=host, user=user, passwd=passwd, db=db)
        self.conn.select_db(self.db)
        self.cursor = self.conn.cursor()

    def close_all(self):
        '''关闭游标和数据库'''
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

    def create_db(self, name):
        '''创建数据库'''
        self.cursor.execute('CREATE DATABASE IF NOT EXISTS py_sql DEFAULT CHARSET \
        utf8 COLLATE utf8_general_ci;')
        print("成功创建" + name + "数据库！")

    def create_table(self, sql):
        '''创建数据表'''
        # 参考sql语句
        '''sql = """CREATE TABLE IF NOT EXISTS `student` (
            `id` int(11) NOT NULL AUTO_INCREMENT,
            `name` varchar(255) NOT NULL,
            `age` int(11) NOT NULL,
            PRIMARY KEY (`id`)
            ) INGINE InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=0"""
        '''
        self.cursor.execute(sql)
        print("成功创建数据表！")

    def insert_one(self, sql):
        '''插入数据'''
        res = self.cursor.execute(sql)
        print("插入成功~共有%d行被改变" % res)

    def insert_many(self, table_name, data):
        '''插入多条数据'''
        sql = "insert into " + table_name + " values(%s,%s,%s)"
        res = self.cursor.executemany(sql, data)
        print("插入成功~共有%d行被改变" % res)

    def select_one(self, table_name, user_name):
        '''查询单条数据'''
        self.cursor.execute("select * from " + table_name)
        while True:
            res = self.cursor.fetchone()
            if res is None:
                print("查无此人~")
                break
            if res[1] == user_name:
                print(res)
                break

    def select_many(self, table_name, row):
        '''查询前n条数据'''
        self.cursor.execute("select * from " + table_name)
        res = self.cursor.fetchmany(row)
        for one in res:
            print(one)

    def select_all(self, table_name):
        '''查询全部数据'''
        self.cursor.execute("select * from " + table_name)
        res = self.cursor.fetchall()
        print("--共查询到%d条数据-----" % len(res))
        for one in res:
            print(one)

    def update_one(self, sql):
        '''更新单条数据'''
        # sql模板 : update 表名 set 字段名=新的值 where 字段名=条件值
        self.cursor.execute(sql)
        print("更新成功~")

    def update_many(self, sql, data):
        '''更新多条数据'''
        # sql模板  : update 表名 set 字段名=%s where 字段名=%s
        # data模板 : [(新的值1, 条件值1), (新的值2, 条件值2), ...]
        row = self.cursor.executemany(sql, data)
        print("更新成功~共有%d行被影响" % row)

    def delete_one(self, table_name, user_name):
        '''删除单条数据'''
        # sql模板 : delete from 表名 where 字段名=条件值
        sql = "delete from " + table_name + " where name='" + user_name + "'"
        res = self.cursor.execute(sql)
        if res != 0:
            print("删除成功~共有%d行被影响" % res)
        if res == 0:
            print("删除失败~该表找不到这条数据")

    def delete_many(self, table_name, field, data):
        '''删除多条数据'''
        # sql模板 : delete from 表名 where 字段名=%s
        # data模板 : [(删除值1), (删除值2), ...]
        sql = "delete from " + table_name + " where " + field + "=%s"
        res = self.cursor.executemany(sql, data)
        if res != 0:
            print("删除成功~共有%d行被影响" % res)
        if res == 0:
            print("删除失败~该表找不到这条数据")

    def rollback(self):
        '''事务回滚'''
        self.conn.rollback()
