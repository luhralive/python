# 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
import x0001
import pymysql

def store_mysql(codelist):
    try:
        conn = pymysql.connect(host="192.168.100.123",user="root",password="mysql123",db="mysql",port=3306)
        cur = conn.cursor()
    except BaseException as e:
        print(e)
    else:
        try:
            cur.execute('CREATE DATABASE IF NOT EXISTS pydb_test')
            cur.execute('use pydb_test')
            sql = '''CREATE TABLE IF NOT EXISTS ACcode(
                id INT NOT NULL AUTO_INCREMENT,
                code VARCHAR(64) NOT NULL,
                primary key (id)
            )'''
            cur.execute(sql)

            for ch in list1:
                cur.execute('INSERT INTO ACcode (code) values (%s)', (ch) )
            cur.connection.commit()
        except BaseException as e:
            print(e)
    finally:
        cur.close()
        conn.close()

if __name__=='__main__':
    list1  = x0001.get_ACCode()
    store_mysql(list1)

