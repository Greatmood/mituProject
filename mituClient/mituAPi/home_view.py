#!/usr/bin/python3
# coding: utf-8

from flask import jsonify
from flask_restful import Resource

from . import home


@home.resource("home/")
class HomePage(Resource):
    def get(self):
        return jsonify({"主页": "home"})