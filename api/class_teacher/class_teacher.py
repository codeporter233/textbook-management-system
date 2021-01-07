from utils.exceptions import custom_abort
from utils.jwt_utils import generate_jwt
from flask import request
from mysql_connect import cursor
import hashlib
from private_settings import mysql_host, mysql_password, mysql_user
import pymysql
import mysql_connect
from . import api

@api.route("/teacher", methods=["GET"])
def select_info():
    print(123)
    hel = mysql_connect()
    cur = hel[1].cursor()
    cur.execute("select * from teacher_id")
    result=cursor.fetchall()
    print(result)
    cur.close()
    return {
        "code": 0
    }

# def user_insertData(number, name, pw, age):
#     achievement_infoData(number, name)
#     hel = user_opendb()
#     hel[1].execute("insert into student_info(student_number,student_name, student_passworld,age)values (?,?,?,?)",
#                    (number, name, pw, age))
#         hel[1].commit()
#         hel[1].close()




