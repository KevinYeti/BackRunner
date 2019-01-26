#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2019/1/26 6:21 AM

__author__ = 'Miracle'

from flask import Flask

from api.v1 import api
from pages.scores import scores
from config.gconfig import gconfig


def create_app():
    app = Flask(__name__, static_folder=gconfig.STATIC_PATH, template_folder=gconfig.TEMPLATE_PATH)
    register_bp(app)
    return app


def register_bp(app):
    app.register_blueprint(api)
    app.register_blueprint(scores)
