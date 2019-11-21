#!/usr/bin/python3
# coding: utf-8

from flask import jsonify
from flask_restful import Resource

from . import destination


@destination.resource('destination/')
class Destination(Resource):
    def get(self):
        return jsonify({"destination": "目的地"})

