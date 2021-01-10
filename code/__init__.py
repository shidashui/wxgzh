# -*- coding: utf-8 -*-
# @Time    : 1/8/2021 11:01 AM
# @Author  : Shui
# @FileName: __init__.py
# @Software: PyCharm

from flask import Flask
from .robot import myrobot
from werobot.contrib.flask import make_view

app = Flask(__name__)
app.add_url_rule(rule='/robot/', # WeRoBot 挂载地址
                 endpoint='werobot', # Flask 的 endpoint
                 view_func=make_view(myrobot),
                 methods=['GET', 'POST'])


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
