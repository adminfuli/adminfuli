#数据库操作
import pymysql
from pymysql.cursors import DictCursor
class Db_handler():
    def __init__(self,host='',
                            port=3306,
                            user='',
                            password='',
                            charset='utf8',
                            database='',
                            cursorclass=DictCursor):
        self.con=pymysql.connect(host=host,
                            port=port,
                            user=user,
                            password=password,
                            charset=charset,
                            database=database,
                            cursorclass=cursorclass)
    # 查询的操作
    def query(self,sql,one=True,):
        self.cursor = self.con.cursor()
        self.cursor.execute(sql)
        if one==True:
            self.con.commit()
            data=self.cursor.fetchone()
            self.cursor.close()
            return data
        else:
            self.con.commit()
            data_all=self.cursor.fetchall()
            self.cursor.close()
            return  data_all
#    插入的操作
    def insert(self,sql):
        self.cursor.execute(sql)
        self.con.commit()
# 关闭的操作
    def close(self):
        self.con.close()
        return ('关闭成功')
if __name__ == '__main__':
    db_handler=Db_handler(host='8.129.91.152',
                            user='future',
                            password='123456',
                            database='futureloan')
    print(db_handler.query(one=False,sql='select leave_amount from member where id=1000337779'))
    print(db_handler.close())