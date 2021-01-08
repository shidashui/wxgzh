# -*- coding: utf-8 -*-
# @Time    : 1/8/2021 11:01 AM
# @Author  : Shui
# @FileName: __init__.py
# @Software: PyCharm

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
