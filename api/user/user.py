import hashlib
from datetime import datetime, timedelta

from flask import request

from mysql_connect import cursor, db
from utils.decorators.cache import cache
from utils.decorators.jwt import token_required
from utils.exceptions import custom_abort
from utils.jwt_utils import generate_jwt
from . import api


@api.route("/login", methods=["GET"])
def handle_login():
    user_id = request.args.get("user_id")
    password = request.args.get("password")
    pwd_md5 = hashlib.md5(password.encode()).hexdigest()
    # 0无此用户， 1管理员用户，2教师用户
    flag = 0
    sql_admin = "select * from admin"
    cursor.execute(sql_admin)
    admins = cursor.fetchall()
    for admin in admins:
        if user_id == admin[0] and pwd_md5 == admin[2]:
            flag = 1
            break
    sql_teacher = "select * from teacher"
    cursor.execute(sql_teacher)
    teachers = cursor.fetchall()
    for teacher in teachers:
        if user_id == teacher[0] and pwd_md5 == teacher[4]:
            flag = 2
            break
    if flag == 1:
        return {
            "code": 0,
            "token": generate_jwt({"user_id": user_id}, datetime.utcnow() + timedelta(days=0, seconds=60 * 10)),
            "authority": "admin"
        }
    elif flag == 2:
        return {
            "code": 0,
            "token": generate_jwt({"user_id": user_id}, datetime.utcnow() + timedelta(days=0, seconds=60 * 10)),
            "authority": "common"
        }
    else:
        custom_abort(-2, "用户名或密码错误")


@api.route("/add_teacher", methods=["GET"])
@token_required
def handle_add_teacher():
    # 获取教师的五个参数
    teacher_id = request.args.get("teacher_id")
    name = request.args.get("name")
    sex = request.args.get("sex")
    telephone = request.args.get("telephone")
    password = request.args.get("password")
    # pwd_md5为加密后的密码,数据库存放的是加密后的密码
    pwd_md5 = hashlib.md5(password.encode()).hexdigest()
    if sex != "男" and sex != "女":
        # 如果性别不为男或女,则抛出异常,在index.py里有处理异常,这个你们不用管
        custom_abort(-3, "性别必须为男或女")
    # 一句sql语句
    sql = "INSERT INTO `textbook_system`.`teacher`(`teacher_id`, `name`, `sex`, `telephone`, `password_md5`) VALUES ('{}', '{}', '{}', '{}', '{}')".format(
        teacher_id, name, sex, telephone, pwd_md5)
    # 执行sql语句，cursor为从mysql_connect导入的
    cursor.execute(sql)
    db.commit()
    # 返回结果，code为0表示运行正常
    return {
        "code": 0
    }


@api.route("delete_teacher", methods=["GET"])
@token_required
def handle_delete_teacher():
    teacher_id = request.args.get("teacher_id")
    sql_select = "select * from teacher where teacher_id='{}'".format(teacher_id)
    cursor.execute(sql_select)
    res = cursor.fetchall()
    if len(res) == 0:
        return {
            "code": -4,
            "message": "无此用户！"
        }
    sql = "delete from teacher where teacher_id='{}'".format(teacher_id)
    cursor.execute(sql)
    db.commit()
    return {
        "code": 0
    }


@api.route("update_teacher", methods=["GET"])
@token_required
def handle_update_teacher():
    teacher_id = request.args.get("teacher_id")
    sql_select = "select * from teacher where teacher_id='{}'".format(teacher_id)
    cursor.execute(sql_select)
    res = cursor.fetchall()
    if len(res) == 0:
        return {
            "code": -4,
            "message": "无此用户！"
        }
    sql = "update teacher set"
    for key, value in dict(request.args).items():
        if key == "teacher_id" or key == "token" or key == "user_id":
            continue
        if key == 'password':
            sql += " password_md5='{}',".format(hashlib.md5(value.encode()).hexdigest())
            continue
        sql += " {}='{}',".format(key, value)
    sql = sql[:-1]
    sql += " where teacher_id='{}'".format(teacher_id)
    cursor.execute(sql)
    db.commit()
    return {
        "code": 0
    }


@api.route("select_teacher", methods=["GET"])
@cache
@token_required
def handle_select_teacher():
    sql = "select * from teacher"
    cursor.execute(sql)
    res = cursor.fetchall()
    data = []
    for i in res:
        data.append(list(i))
    return {
        "code": 0,
        "data": data
    }
