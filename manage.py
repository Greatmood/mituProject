#!/usr/bin/python3
# coding: utf-8
from flask_script import Manager

from mituClient import create_app

app = create_app
manage = Manager(app)


if __name__ == '__main__':
    manage.run()