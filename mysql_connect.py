import pymysql

from private_settings import mysql_host, mysql_password, mysql_user

db = pymysql.connect(mysql_host, mysql_user, mysql_password, "textbook_system", charset='utf8')
cursor = db.cursor()
