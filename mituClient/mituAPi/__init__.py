#!/usr/bin/python3
# coding: utf-8

from flask import Blueprint
from flask_restful import Api

home_bp = Blueprint("home", __name__, url_prefix="/api/")
mine_bp = Blueprint("mine", __name__, url_prefix="/api/")
discover_bp = Blueprint("discover", __name__, url_prefix="/api/")
destination_bp = Blueprint("destination", __name__, url_prefix="/api/")


home = Api(home_bp)
mine = Api(mine_bp)
discover = Api(discover_bp)
destination = Api(destination_bp)

from . import home_view, mine_view, discover_view, destination_view