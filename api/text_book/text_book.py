import hashlib
from datetime import datetime, timedelta

from flask import request

from mysql_connect import cursor, db
from utils.decorators.jwt import token_required
from utils.exceptions import custom_abort
from utils.jwt_utils import generate_jwt
from . import api


@api.route("/insert_T", methods=["GET"])
def handle_insert_T():
    book_id = request.args.get("book_id")
    book_name = request.args.get("subscribe_count")
    author = request.args.get("subscribe_time")
    press = request.args.get("attribute_time")
    sql = "insert into textbook(book_id, book_name, author, press) values ('{}','{}','{}','{}')".format(book_id,
                                                                                                        book_name,
                                                                                                        author,
                                                                                                        press)

    cursor.execute(sql)
    db.commit()
    return {
        "code": 0,
    }


@api.route("/insert_as", methods=["GET"])
def handle_insert_T():
    book_id = request.args.get("book_id")
    class_id = request.args.get("class_id")
    teacher_id = request.args.get("teacher_id")
    sql_select = "select 1 from textbook where book_id = '{}' limit 1".format(book_id)
    cursor.execute(sql_select)
    select_list = cursor.fetchall()
    if select_list is 1:
        sql = "insert into attribution_subscribe(book_id,class_id,teacher_id) values ('{}','{}','{}')".format(
            book_id,
            class_id,
            teacher_id)
    cursor.execute(sql)
    db.commit()
    return {
        "code": 0,
    }


@api.route("/select", methods=["GET"])
def handle_select():
    sql = "select * from attribution_subscribe where 1=1 "
    book_id = request.args.get("book_id")
    class_id = request.args.get("class_id")
    teacher_id = request.args.get("teacher_id")
    subscribe_time = request.args.get("subscribe_time")
    if book_id is not None:
        sql += "and book_id like '%" + book_id + "%'"
    if class_id is not None:
        sql += "and class_id like '%" + class_id + "%'"
    if teacher_id is not None:
        sql += "and teacher_id like '%" + teacher_id + "%'"
    if subscribe_time is not None:
        sql += "and subscribe_time like '%" + subscribe_time + "%'"
    cursor.execute(sql)
    select_list = cursor.fetchall()
    data = []
    for res in select_list:
        temp = list(res)
        temp[5] = str(temp[5])
        temp[6] = str(temp[6])
        data.append(temp)
    return {
        "code": 0,
        "data": select_list
    }


@api.route("/update_T", methods=["GET"])
def handle_update_T():
    book_id = request.args.get("book_id")
    book_name = request.args.get("book_name")
    author = request.args.get("author")
    press = request.args.get("press")
    sql = "update textbook set book_name='{}', author='{}',press='{}' where book_id='{}'".format(book_name, author,
                                                                                                 press, book_id)
    cursor.execute(sql)
    db.commit()
    return {
        "code": 0,
    }


@api.route("/update_as", methods=["GET"])
def handle_update_as():
    book_id = request.args.get("book_id")
    class_id = request.args.get("class_id")
    teacher_id = request.args.get("teacher_id")
    subscribe_time = request.args.get("subscribe_time")
    sql_select = "select 1 from textbook where book_id = '{}' limit 1".format(book_id)
    cursor.execute(sql_select)
    select_list = cursor.fetchall()
    if select_list is 1:
        sql = "update attribution_subscribe set class_id='{}',teacher_id='{}',subscribe_time='{}' where book_id='{}'".format(
            class_id,
            teacher_id,
            datetime.date.today(),
            book_id)
    cursor.execute(sql)
    db.commit()
    return {
        "code": 0,
    }


@api.route("/delete_T", methods=["GET"])
def handle_delete_T():
    book_id = request.args.get("book_id")
    sql = "delete from textbook where book_id='{}'".format(book_id)
    cursor.execute(sql)
    db.commit()
    return {
        "code": 0,
    }


@api.route("/delete_as", methods=["GET"])
def handle_delete_as():
    sql = "delete from attribution_subscribe where 1=1 "
    book_id = request.args.get("book_id")
    class_id = request.args.get("class_id")
    teacher_id = request.args.get("teacher_id")
    if book_id is not None:
        sql = "and book_id='%"+book_id+"%'"
    if class_id is not None:
        sql = "and class_id='%"+class_id+"%'"
    if teacher_id is not None:
        sql = "and teacher_id='%"+teacher_id+"%'"
    cursor.execute(sql)
    print(sql)
    delete_list = cursor.fetchall()
    data = []
    for res in delete_list:
        temp = list(res)
        temp[6] = str(temp[6])
        temp[7] = str(temp[7])
        data.append(temp)
    return {
        "code": 0,
        "data": delete_list
    }

