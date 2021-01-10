# -*- coding: utf-8 -*-
# @Time    : 1/9/2021 10:32 AM
# @Author  : Shui
# @FileName: robot.py
# @Software: PyCharm

from werobot import WeRoBot

myrobot = WeRoBot(token='token')


@myrobot.handler
def hello(message):
    return 'Hello World!'