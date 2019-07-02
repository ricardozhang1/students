#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 11:04
# @Author  : ZhangChaowei
# @Site    : 
# @File    : dev.py
# @Software: PyCharm


from . import Config


class DevelopmentConfig(Config):
    """开发模式下的配置"""
    # 查询时会显示原始SQL语句
    SQLALCHEMY_ECHO = True





