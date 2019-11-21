#!/usr/bin/python3
# coding: utf-8

from flask import Flask
from flask_cors import CORS
from settings import config
from mituClient.mituAPi import home_bp, mine_bp, discover_bp, destination_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_bp)
    app.register_blueprint(mine_bp)
    app.register_blueprint(discover_bp)
    app.register_blueprint(destination_bp)
    app.config.from_object(config["development"])
    CORS(app)
    return app