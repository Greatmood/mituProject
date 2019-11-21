#!/usr/bin/python3
# coding: utf-8

from flask import jsonify
from flask_restful import Resource

from . import mine


@mine.resource('mine/')
class MinePage(Resource):
    def get(self):
        return jsonify({"我的": "mine"})


@mine.resource('login/')
class Login_in(Resource):
    def post(self):
        return jsonify({
            "method": "POST",
            "msg": "登陆成功",
            "data": {
                "id": "*********",
                "name": "张三",
                "token": "************"
            }
        })
