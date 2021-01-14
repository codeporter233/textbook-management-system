from flask import request

from mysql_connect import cursor, db
from utils.decorators.cache import cache
from . import api


# 教师班级表查询
@api.route("/select_teacher_class", methods=["GET"])
@cache
def select_class_id():
    sql = "select * from teacher_class WHERE 1=1 "
    select_teacner_id = request.args.get("teacher_id")
    select_class_id = request.args.get("class_id")
    select_course_id = request.args.get("course_id")
    if select_teacner_id != "":
        sql += "and teacher_id like '%" + select_teacner_id + "%'"
    if select_class_id != "":
        sql += "and class_id like '%" + select_class_id + "%'"
    if select_course_id != "":
        sql += "and course_id like '%" + select_course_id + "%'"
    print(sql)
    cursor.execute(sql)
    result = cursor.fetchall()
    data = []
    for i in result:
        data.append(list(i))
    return {
        "code": 0,
        "data": data

    }


# 教师班级表插入
@api.route("/insert_teacher_class", methods=["GET"])
def teacher_class_insertData():
    insert_class_id = request.args.get("class_id")
    insert_teacher_id = request.args.get("teacher_id")
    insert_course_id = request.args.get("course_id")
    sql = "insert into teacher_class(teacher_id,class_id,course_id)VALUES('{}','{}','{}')".\
        format(insert_teacher_id,insert_class_id,insert_course_id)
    cursor.execute(sql)
    db.commit()
    return {
        "code": 0
    }


# 教师班级表删除
@api.route("/delete_teacher_class", methods=["GET"])
def teacher_class_deleteData():
    sql = "delete from teacher_class WHERE 1=1 "
    teacher_id1 = request.args.get("teacher_id")
    class_id1 = request.args.get("class_id")
    course_id1 = request.args.get("course_id")
    if teacher_id1 is not None:
        sql += "and teacher_id like '" + teacher_id1 + "'"
    if class_id1 is not None:
        sql += "and class_id like '" + class_id1 + "'"
    if course_id1 is not None:
        sql += "and course_id like '" + course_id1 + "'"
    cursor.execute(sql)
    db.commit()
    return {
        "code": 0
    }


# 教师班级表修改
@api.route("/update_teacher_class", methods=["GET"])
def teacher_class_updateData():
    old_class_id = request.args.get("old_class_id")
    new_class_id = request.args.get("new_class_id")
    old_teacher_id = request.args.get("old_teacher_id")
    new_teacher_id = request.args.get("new_teacher_id")
    old_course_id = request.args.get("old_course_id")
    new_course_id = request.args.get("new_course_id")
    sql = "update teacher_class set class_id='{}' ,teacher_id='{}', course_id='{}' where class_id='{}' and teacher_id='{}' and course_id='{}'".format(
        new_class_id, new_teacher_id, new_course_id, old_class_id, old_teacher_id, old_course_id)
    cursor.execute(sql)
    db.commit()
    return {
        "code": 0
    }
