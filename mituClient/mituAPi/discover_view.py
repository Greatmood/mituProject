#!/usr/bin/python3
# coding: utf-8

from flask import jsonify
from flask_restful import Resource

from . import discover


@discover.resource("discover/")
class DiscoverPage(Resource):
    def get(self):
        return jsonify({"discover": "发现"})



@discover.resource("article/")
class Article(Resource):

    data = {
        "id": 1,
        "nick_name": "李四",
        "user_short_info": "喜欢玩",
        "article_title": "兵马俑一日游",
        "article_url": "http://......",
        "artticle_img": "http://......",
        "点赞数": "50",
        "浏览量": "100"}

    def get(self):
        l1 = []
        for _ in range(10):
            l1.append(self.data)


        return jsonify({
                "methon": "GET",
                "refer" : "url",
                "data" : l1

            })