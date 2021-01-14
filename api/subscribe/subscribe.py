from datetime import datetime

from flask import request

from mysql_connect import cursor, db
from . import api


@api.route("/insert_attribution_subscribe", methods=["GET"])
def handle_insert_attribution_subscribe():
    book_id = request.args.get("book_id")
    class_id = request.args.get("class_id")
    teacher_id = request.args.get("teacher_id")
    subscribe_count = request.args.get("subscribe_count")
    subscribe_time = request.args.get("subscribe_time")
    # 如果存在 可以添加as表信息
    sql = "insert into attribution_subscribe(book_id,class_id,teacher_id,subscribe_count, subscribe_time) " \
          "values ('{}','{}','{}','{}','{}')".format(book_id, class_id, teacher_id, subscribe_count, subscribe_time)
    cursor.execute(sql)
    db.commit()
    return {
        "code": 0,
    }


@api.route("/select_attribution_subscribe", methods=["GET"])
def handle_select():
    sql = "select * from attribution_subscribe where 1=1 "
    book_id = request.args.get("book_id")
    class_id = request.args.get("class_id")
    teacher_id = request.args.get("teacher_id")
    subscribe_time = request.args.get("subscribe_time")
    if book_id is not None:
        sql += "and book_id like '%{}%'".format(book_id)
    if class_id is not None:
        sql += "and class_id like '%{}%'".format(class_id)
    if teacher_id is not None:
        sql += "and teacher_id like '%{}%'".format(teacher_id)
    if subscribe_time is not None:
        sql += "and subscribe_time like '%{}%'".format(subscribe_time)
    print(sql)
    cursor.execute(sql)
    select_list = cursor.fetchall()
    data = []
    for res in select_list:
        temp = list(res)
        temp[4] = str(temp[4])
        temp[5] = str(temp[5])
        data.append(temp)
    return {
        "code": 0,
        "data": select_list
    }


@api.route("/update_attribution_subscribe", methods=["GET"])
def handle_update_attribution_subscribe():
    book_id = request.args.get("book_id")
    class_id = request.args.get("class_id")
    teacher_id = request.args.get("teacher_id")
    count = request.args.get("subscribe_count")
    sql = "update attribution_subscribe set subscribe_count='{}' where book_id='{}' and class_id='{}' and teacher_id='{}'" \
        .format(count, book_id, class_id, teacher_id)
    cursor.execute(sql)
    db.commit()
    return {
        "code": 0,
    }


@api.route("/delete_attribution_subscribe", methods=["GET"])
def handle_delete_attribution_subscribe():
    book_id = request.args.get("book_id")
    class_id = request.args.get("class_id")
    teacher_id = request.args.get("teacher_id")
    sql = "delete from attribution_subscribe where book_id='{}' and class_id='{}' and teacher_id='{}'".format(book_id, class_id, teacher_id)
    print(sql)
    cursor.execute(sql)
    db.commit()
    return {
        "code": 0,
    }
