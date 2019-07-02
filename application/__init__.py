#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 11:04
# @Author  : ZhangChaowei
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm

from flask import Flask
from application.settings.dev import DevelopmentConfig
from application.settings.prop import ProductionConfig
from redis import StrictRedis
from flask_wtf import CSRFProtect
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import logging
from logging.handlers import RotatingFileHandler

config = {
    "dev": DevelopmentConfig,
    "prop": ProductionConfig,
}

redis_store = None
db = SQLAlchemy()


def init_app(config_name):
    """项目初始化函数"""
    app = Flask(__name__)

    # 设置配置类
    Config = config[config_name]  # 名字传进来的时候，会调用类

    # 加载配置项
    app.config.from_object(Config)  # Config是一个类配置

    # redis的连接初始化
    global redis_store
    redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=0)

    # 开启CSR防范功能
    CSRFProtect(app)

    # 开启Session功能
    Session(app)

    # 启用日志功能
    setup_log(Config)

    # 配置数据库连接
    db.init_app(app)

    # TODO注册蓝图对象到app应用中
    # 首页模块
    from .apps.index import index_blu
    app.register_blueprint(index_blu, url_prefix="")

    return app


def setup_log(Config):
    # 设置日志的记录等级
    logging.basicConfig(level=Config.LOG_LEVEL)

    # 创建日志记录器，指明日志保存的路径，每个日志文件的最大大小，保存日志文件个数上限
    file_log_hander = RotatingFileHandler("logs/log", maxBytes=1024*1024*300, backupCount=10)
    # 创建日志记录的格式，日志等级，输出日志信息的文件名 行数 日志信息
    formatter = logging.Formatter("%(levelname)s %(filename)s: %(lineno)d %(message)s")

    # 为刚创建的日志记录器设置日志记录格式
    file_log_hander.setFormatter(formatter)
    # 为全局的日志工具对象(flaskapp使用的)添加日志记录器
    logging.getLogger().addHandler(file_log_hander)
