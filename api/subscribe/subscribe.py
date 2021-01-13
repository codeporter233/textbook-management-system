from datetime import datetime

from flask import request

from mysql_connect import cursor, db
from . import api


@api.route("/insert_attribution_subscribe", methods=["GET"])
def handle_insert_attribution_subscribe():
    '''插入不重复'''
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


@api.route("/update_attribution_subscribe", methods=["GET"])
def handle_update_attribution_subscribe():
    book_id = request.args.get("book_id")
    class_id = request.args.get("class_id")
    teacher_id = request.args.get("teacher_id")
    sql_select = "select attribute_time from attribution_subscribe where book_id = '{}' and class_id = '{}' ".format(
        book_id, class_id)
    cursor.execute(sql_select)
    select_list = cursor.fetchall()
    # 循环多行
    for item in select_list:
        # 现在日期-发放日期 大于1天才能修改
        # (datetime.datetime(2021, 1, 10, 0, 0),)
        # is_bool = abs(datetime.now()-item[0]) > timedelta(days=1) #True 大于或者小于1天
        is_bool = datetime.now() < item[0]  # True 如果当前时间小于attr
        if is_bool:  # 判断日期是否超过一天
            sql = "update attribution_subscribe set class_id='{}',teacher_id='{}',subscribe_time='{}' where book_id='{}'" \
                .format(class_id, teacher_id, datetime.now().date(), book_id)
            cursor.execute(sql)
            db.commit()
    return {
        "code": 0,
    }


@api.route("/delete_attribution_subscribe", methods=["GET"])
def handle_delete_attribution_subscribe():
    book_id = request.args.get("book_id")
    class_id = request.args.get("class_id")
    sql_select = "select attribute_time from attribution_subscribe where book_id = '{}' and class_id = '{}' ".format(
        book_id, class_id, )
    cursor.execute(sql_select)
    select_list = cursor.fetchall()
    # 循环多行
    for item in select_list:
        # 现在日期-发放日期 大于1天才能修改
        # (datetime.datetime(2021, 1, 10, 0, 0),)
        # is_bool = abs(datetime.now()-item[0]) > timedelta(days=1) #True 大于或者小于1天
        is_bool = datetime.now() < item[0]  # True 如果当前时间小于attr
        if is_bool:  # 判断日期是否超过一天
            sql = "delete from attribution_subscribe where book_id='{}' and class_id='{}'".format(book_id, class_id)
            cursor.execute(sql)
            db.commit()
    return {
        "code": 0,
    }
