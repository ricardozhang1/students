#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 11:07
# @Author  : ZhangChaowei
# @Site    : 
# @File    : views.py
# @Software: PyCharm

from . import index_blu
from .models import Student
from flask import request, render_template
from application import db
from flask import flash
from json import dumps


@index_blu.route("/search")
def index():
    """学生列表"""
    student_list = Student.query.all()
    data = []
    for student in student_list:
        print(student.sex)
        data.append({
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "sex": student.sex,
            "description": student.description,
            "class_number": student.class_number,
        })
    return render_template("index.html", students=data)
    # return dumps({{item["id"]: item} for item in data})


@index_blu.route("/add", methods=["POST", "GET"])
def add_student():
    if request.method == "POST":
        # 接受数据
        name = request.form.get("username")
        age = int(request.form.get("age"))
        sex = True if request.form.get("sex") == '1' else False
        class_number = request.form.get("class_number")
        description = request.form.get("description")
        print(name, age, sex, class_number, description)
        # 验证数据
        if age < 0 or age > 120:
            flash("非法的年龄数值")
        # 保存入库
        student = Student(
            name=name,
            age=age,
            sex=sex,
            class_number=class_number,
            description=description,
        )
        try:
            db.session.add(student)
            db.session.commit()
            return "数据提交成功"
        except:
            # 事务回滚
            db.session.rollback()
            return "数据提交失败"

    return render_template('add.html')









