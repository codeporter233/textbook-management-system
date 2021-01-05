from utils.exceptions import custom_abort
from utils.jwt_utils import generate_jwt
from . import api
from flask import request
from mysql_connect import cursor
import hashlib


@api.route("/login", methods=["GET"])
def handle_login():
    name = request.args.get("user_id")
    password = request.args.get("password")
    pwd_md5 = hashlib.md5(password.encode()).hexdigest()
    sql = "select * from master"
    cursor.execute(sql)
    users = cursor.fetchall()
    flag = 0
    for user in users:
        if name == user[1] and pwd_md5 == user[2]:
            flag = 1
            break
    if flag == 1:
        return {
            "code": 0,
            "token": generate_jwt({"name": name})
        }
    else:
        custom_abort(-2, "用户名或密码错误")



