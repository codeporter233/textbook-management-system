from flask import request

from mysql_connect import cursor, db
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
    db.commit()
    return {
        "code": 0
    }


@api.route("/attribution_query", methods=["GET"])
def attribution_query():
    sql = "select * from attribution_subscribe where 1=1"
    for key, value in dict(request.args).items():
        sql += " and {} like '%{}%'".format(key, value)
    cursor.execute(sql)
    db.commit()
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
