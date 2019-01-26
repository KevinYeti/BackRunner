#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2019/1/26 7:50 AM

__author__ = 'Miracle'


import os

class Base:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    STATIC_PATH = os.path.join(BASE_DIR, 'static')
    TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

class Dev(Base):
    pass




gconfig = Dev