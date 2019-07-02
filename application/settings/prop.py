#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 11:05
# @Author  : ZhangChaowei
# @Site    : 
# @File    : prop.py
# @Software: PyCharm

from . import Config


class ProductionConfig(Config):
    """生产模式下的配置"""
    DEBUG = False






