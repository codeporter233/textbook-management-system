from flask import request

from mysql_connect import cursor
from . import api
import datetime


@api.route("/record", methods=["GET"])
def record_attribution():
    class_id = request.args.get("class_id")
    book_id = request.args.get("book_id")
    count = request.args.get("attribution_count")
    if count is None:
        sql = "select count from class where class_id={}".format(class_id)
        cursor.execute(sql)
        count = cursor.fetchall()[0][0]
    sql = "select monitor from class where class_id={}".format(class_id)
    cursor.execute(sql)
    monitor = cursor.fetchall()[0][0]
    curr_time = datetime.datetime.now()
    time_str = curr_time.strftime("%Y-%m-%d %H:%M:%S")
    sql = "update attribution_subscribe set attribute_time='{}',attribute_count='{}',receiver_name='{}' where class_id='{}' and book_id='{}'".format(
        time_str, count, monitor, class_id, book_id)
    cursor.execute(sql)
    return {
        "code": 0
    }


@api.route("/attribution_query", methods=["GET"])
def attribution_query():
    sql = "select * from attribution_subscribe where 1=1 "
    class_id = request.args.get("class_id")
    book_id = request.args.get("book_id")
    attribute_time = request.args.get("attribute_time")
    subscribe_time = request.args.get("subscribe_time")
    course_id = request.args.get("course_id")
    teacher_id = request.args.get("teacher_id")
    receiver = request.args.get("receiver")
    if class_id is not None:
        sql += "and class_id like '%" + class_id + "%'"
    if book_id is not None:
        sql += "and book_id like '%" + book_id + "%'"
    if teacher_id is not None:
        sql += "and teacher_id like '%" + teacher_id + "%'"
    if course_id is not None:
        sql += "and course_id like '%" + course_id + "%'"
    if attribute_time is not None:
        sql += "and attribute_time like '%" + attribute_time + "%'"
    if subscribe_time is not None:
        sql += "and subscribe_time like '%" + subscribe_time + "%'"
    if receiver is not None:
        sql += "and receiver_name like '%" + receiver + "%'"
    cursor.execute(sql)
    query_results = cursor.fetchall()
    data = []
    for res in query_results:
        temp = list(res)
        temp[4] = str(temp[4])
        temp[5] = str(temp[5])
        data.append(temp)
    return {
        "code": 0,
        "data": data
    }
