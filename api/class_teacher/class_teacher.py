from utils.exceptions import custom_abort
from utils.jwt_utils import generate_jwt
from flask import request
import hashlib
from private_settings import mysql_host, mysql_password, mysql_user
import pymysql
import mysql_connect
from mysql_connect import cursor, db
from . import api

# 班级表
@api.route("/class", methods=["GET"])
def select_info():
    sql="select * from class"
    cursor.execute(sql)
    result=cursor.fetchall()
    print(result)
    return {
        "code": 0,
        "result":result

    }
# 班级表查询
@api.route("/select_class", methods=["GET"])
def select_class():
    sql ="select * from class WHERE 1=1"
    class_number = request.args.get("class_id")
    class_monitor = request.args.get("class_monitor")
    class_count = request.args.get("class_count")
    if class_number is not None:
        sql += "and class_id like '"+ class_number + "'"
    if class_monitor is not None:
        sql += "and monitor like '"+ class_monitor + "'"
    if class_count is not None:
        sql += "and count like '"+ class_count + "'"
    cursor.execute(sql)
    result=cursor.fetchall()

    if len(result) == 0:
        print("查询异常")
    print(result)
    return {
        "code": 0,
        "result":result

    }
# 班级表插入
@api.route("/insert_class", methods=["GET"])
def class_insertData():
    class_number = request.args.get("class_id")
    monitor = request.args.get("monitor")
    sum = request.args.get("sum")
    # sql="insert into class(class_number,monitor,sum)VALUES(?,?,?)" ,(class_number,monitor,sum)
    sql="insert into class(class_id,monitor,count)VALUES('{}','{}','{}')" .format(class_number,monitor,sum)
    cursor.execute(sql)
    return {
        "code": 0

    }
# 班级表删除
@api.route("/delete_class", methods=["GET"])
def class_deleteData():
    sql = "delete from class WHERE 1=1"
    class_number = request.args.get("class_id")
    class_monitor = request.args.get("class_monitor")
    class_count = request.args.get("class_count")
    if class_number is not None:
        sql += "and class_id like '" + class_number + "'"
    if class_monitor is not None:
        sql += "and monitor like  '" + class_monitor + "'"
    if class_count is not None:
        sql += "and count like '" +class_count+ "'"
    cursor.execute(sql)
    return {
        "code": 0

    }
# 班级表修改
@api.route("/update_class", methods=["GET"])
def class_updateData():
    old_class_id = request.args.get("old_class_id")
    new_class_id = request.args.get("new_class_id")
    old_monitor = request.args.get("old_monitor")
    new_monitor = request.args.get("new_monitor")
    old_count = request.args.get("old_count")
    new_count = request.args.get("new_count")
    sql="update class set class_id='{}',monitor='{}',count='{}' where class_id='{}' and monitor='{}' and count='{}' ".format(new_class_id,new_monitor,new_count,old_class_id,old_monitor,old_count)
    cursor.execute(sql)
    return {
        "code": 0
    }
@api.route("/select_teacher_class", methods=["GET"])
# 教师班级表
def select_all():
    sql="select * from teacher_class"
    cursor.execute(sql)
    result=cursor.fetchall()
    print(result)
    return {
        "code": 0,
        "result":result
    }
# 教师班级表查询
@api.route("/select_teacher_class_id", methods=["GET"])
def select_class_id():
    sql = "select * from teacher WHERE 1=1"
    select_teacner_number = request.args.get("teacher_id")
    select_class_id = request.args.get("class_id")
    select_course_id = request.args.get("course_id")
    if select_teacner_number is not None:
        sql += "and teacher_id like '" + select_teacner_number + "'"
    if select_class_id is not None:
        sql += "and class_id like '" + select_class_id + "'"
    if select_course_id is not None:
        sql += "and course_id like '" + select_course_id + "'"
    cursor.execute(sql)
    result=cursor.fetchall()

    if len(result) == 0:
        print("查询异常")
    print(result)
    return {
        "code": 0,
        "result":result

    }
# 教师班级表插入
@api.route("/insert_teacher_class", methods=["GET"])
def teacher_class_insertData():
    insert_class_id = request.args.get("class_id")
    insert_teacher_id = request.args.get("teacher_id")
    insert_course_id = request.args.get("course_id")

    sql="insert into teacher_class(teacher_id,class_id,course_id)VALUES('{}','{}','{}')" .format(insert_teacher_id,insert_class_id,insert_course_id)
    print(sql)
    cursor.execute(sql)
    db.commit()

    return {
        "code": 0

    }
# 教师班级表删除
@api.route("/delete_teacher_class", methods=["GET"])
def teacher_class_deleteData():
    sql="delete * from teacher_class WHERE 1=1"
    teacher_id1 = request.args.get("teacher_id")
    class_id1 = request.args.get("class_id")
    course_id1 = request.args.get("course_id")
    # sql="delete from teacher_class WHERE teacher_id='{}' and class_id='{}' and course_id='{}'" .format(teacher_id1,class_id1,course_id1)
    if teacher_id1 is not None:
        sql += "and teahcer_id like '" + teacher_id1 + "'"
    if class_id1 is not None:
        sql += "and class_id like '" + class_id1+ "'"
    if course_id1 is not None:
         sql += "and class_id like '" + course_id1 + "'"
    print(sql)
    cursor.execute(sql)
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
    sql="update teacher_class set class_id='{}' ,teacher_id='{}', course_id='{}' where class_id='{}' and teacher_id='{}' and course_id='{}'".format(new_class_id,new_teacher_id,new_course_id,old_class_id,old_teacher_id,old_course_id)

    # sql="update teacher_class set class_id='{}' teacher_id='{}' course_id='{}' where class_id='{}' and teacher_id='{}' and course_id='{}'".format(new_class_id,new_teacher_id,new_course_id,old_course_id,old_teacher_id,old_class_id)
    print(sql)
    cursor.execute(sql)
    return {
        "code": 0
    }
# teacher
@api.route("/teacher", methods=["GET"])
def select_teacher_all():
    sql="select * from teacher"
    cursor.execute(sql)
    result=cursor.fetchall()
    print(result)
    return {
        "code": 0,
        "result":result
    }
# 教师表查询
@api.route("/select_teacher", methods=["GET"])
def select_teacher():
    sql="select * from teacher WHERE 1=1"
    teacher_number = request.args.get("teacher_id")
    teacher_name = request.args.get("teacher_name")
    teacher_sex = request.args.get("teacher_sex")
    teacher_telephone = request.args.get("teacher_telephone")
    teacher_password = request.args.get("teacher_password")
    if teacher_number is not None:
        sql += "and teacher_id like '" + teacher_number + "'"
    if teacher_name is not None:
        sql += "and name like '" + teacher_name + "'"
    if teacher_sex is not None:
        sql += "and sex like '" + teacher_sex + "'"
    if teacher_telephone is not None:
        sql += "and telephone like '" + teacher_telephone + "'"
    if teacher_password is not None:
        sql += "and password_md5 like '" + teacher_password + "'"
    print(sql)
    cursor.execute(sql)
    result=cursor.fetchall()

    if len(result) == 0:
        print("查询异常")
    print(result)
    return {
        "code": 0,
        "result":result

    }
# 教师表插入
@api.route("/insert_teacher", methods=["GET"])
def teacher_insertData():
    teacher_number = request.args.get("teacher_id")
    teacher_name = request.args.get("teacher_name")
    teacher_sex= request.args.get("teacher_sex")
    teacher_telephone = request.args.get("teacher_telephone")
    teacher_password = request.args.get("teacher_password")
    # sql="insert into class(class_number,monitor,sum)VALUES(?,?,?)" ,(class_number,monitor,sum)
    sql="insert into teahcer(teacher_id,name,sex,telephone,password_md5)VALUES('{}','{}','{}','{}','{}')" .format(teacher_number,teacher_name,teacher_sex,teacher_telephone,teacher_password)
    cursor.execute(sql)
    return {
        "code": 0

    }
# 教师表删除
@api.route("/delete_teacher", methods=["GET"])
def teacher_deleteData():
    teacher_number = request.args.get("teacher_id")
    sql="delete from teacher WHERE teacher_id={}" .format(teacher_number)
    cursor.execute(sql)
    return {
        "code": 0

    }
# 教师表修改
@api.route("/update_teacher", methods=["GET"])
def teacher_updateData():
    old_teacher_id = request.args.get("old_teacher_id")
    new_teacher_id = request.args.get("new_teacher_id")
    old_teacher_name = request.args.get("old_teacher_name")
    new_teacher_name = request.args.get("new_teacher_name")
    old_teacher_sex = request.args.get("old_teacher_sex")
    new_teacher_sex = request.args.get("new_teacher_sex")
    old_teacher_password = request.args.get("old_teacher_password")
    new_teacher_password = request.args.get("new_teacher_password")
    old_teacher_telephone = request.args.get("old_teacher_telephone")
    new_teacher_telephone = request.args.get("new_teacher_telephone")

    sql="update teacher set teacher_id='{}',name='{}',sex='{}',telephone'{}',password_md5='{}' where teacher_id='{}' and name='{}' and sex='{}' and telephone='{}' and password='{}' ".format(new_teacher_id,new_teacher_name,new_teacher_sex,new_teacher_telephone,new_teacher_password,old_teacher_id,old_teacher_name,old_teacher_sex,old_teacher_telephone,old_teacher_password)
    print(sql)
    cursor.execute(sql)
    return {
        "code": 0
    }








