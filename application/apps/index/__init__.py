#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 11:06
# @Author  : ZhangChaowei
# @Site    : 
# @File    : __init__.py
# @Software: PyCharm

from flask import Blueprint

index_blu = Blueprint("index_blu", __name__, template_folder="templates")

from .views import *




