#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 11:07
# @Author  : ZhangChaowei
# @Site    : 
# @File    : models.py
# @Software: PyCharm

from application import db


# 创建关系表，不在创建模型，一般用于表与表之间的多对多场景
"""
表关系变量 = db.Table(
    "关系表表名"
    db.Column('字段名', 字段类型, 字段选项), # 普通字段
    db.Column('字段名', 字段类型, db.ForeignKey("表名.id")),
    db.Column('字段名', 字段类型, db.ForeignKey("表名.id")),
)
"""

achievement = db.Table(
    "achievement",
    db.Column('score', db.Numeric, comment="分数"),
    db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
)


class Student(db.Model):
    """学生信息"""
    __tablename__ = "student"
    id = db.Column(db.Integer, primary_key=True, comment="主键ID")
    name = db.Column(db.String(64), index=True, comment="姓名")
    sex = db.Column(db.Boolean, default=True, comment="性别")
    class_number = db.Column(db.String(32), nullable=True, comment="班级")
    age = db.Column(db.SmallInteger, comment="年龄")
    description = db.Column(db.Text, comment="个性签名")
    courses = db.relationship(
        'Course',  # 模型名称
        secondary=achievement,  # 表关系变量
        backref='students',  # 当外键反过来获取主键信息时
        lazy='dynamic'
    )

    def __repr__(self):
        return "%s" % self.name


class Course(db.Model):
    """课程信息"""
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True, comment="主键ID")
    name = db.Column(db.String(64), unique=True, comment="课程名称")

    def __repr__(self):
        return "%s" % self.name




