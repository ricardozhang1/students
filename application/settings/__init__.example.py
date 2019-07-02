#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 11:05
# @Author  : ZhangChaowei
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm

from redis import StrictRedis


class Config(object):
    """项目配置核心类"""
    # 调试模式
    DEBUG = True

    # todo配置日志
    LOG_LEVEL = "DEBUG"

    # mysql数据库的配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://***:***@127.0.0.1:3306/students?charset=utf8"
    # 动态追踪修改设置，如未设置只会提示警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 查询时会显示原始SQL查询语句
    SQLALCHEMY_ECHO = False

    # 配置redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # 设置密钥
    SECRET_KEY = "***"

    # 使用csrf验证，默认是开启的
    # WTF_CSRF_CHECK_DEFAULT = False

    # flask_session的配置信息
    SESSION_TYPE = "redis"
    SESSION_USE_SIGNER = True

    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=10)
    PERMANENT_SESSION_LIFETIME = 24*60*60





