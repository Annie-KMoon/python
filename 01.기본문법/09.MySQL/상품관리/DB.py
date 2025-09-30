#공용 DB
import pymysql

con = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    db='shop',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor,
    port = 3306
    )
cur = con.cursor()