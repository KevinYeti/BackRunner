#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2019/1/26 7:38 AM

__author__ = 'Miracle'

import os

from flask import render_template, Blueprint
from flask.views import MethodView

from config.gconfig import gconfig

scores = Blueprint('scores', __name__, url_prefix='/scores/')


class ScoresView(MethodView):
    def get(self):
        return render_template('scores/scores.html')


scores.add_url_rule('/', view_func=ScoresView.as_view('scores'))
