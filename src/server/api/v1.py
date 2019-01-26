#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2019/1/26 6:20 AM

__author__ = 'Miracle'

from flask import jsonify, Blueprint, request
from flask.views import MethodView

from . import api_prefix

api = Blueprint('api', __name__, url_prefix=api_prefix)
records = []


def register_api(view, endpoint, url, pk='id', pk_type='int'):
    view_func = view.as_view(endpoint)
    api.add_url_rule(url, defaults={pk: None}, view_func=view_func, methods=['GET', ])
    api.add_url_rule(url, view_func=view_func, methods=['POST', ])
    api.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func, methods=['GET', 'PUT', 'DELETE'])


class ScoresAPI(MethodView):

    def get(self, username):
        if username is None:
            return jsonify(dict(
                records=records
            ))
        else:
            # 获取username的分数
            return jsonify(dict(
                username='yang',
                score=90
            ))

    def post(self):
        '''
        注册一条新纪录
        '''
        data = request.json
        username = data.get('username', 'default')
        score = data.get('score', -1)
        records.append((username, score))
        return jsonify(dict(
            code=200,
            msg='',
        ))


register_api(ScoresAPI, 'scores_api', '/scores/', pk='username', pk_type='string')

if __name__ == '__main__':
    pass
