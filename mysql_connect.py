from private_settings import mysql_host, mysql_password, mysql_user
import pymysql

class_db = pymysql.connect(mysql_host, mysql_user, mysql_password, "class", charset='utf8')
class_cursor = class_db.cursor()


