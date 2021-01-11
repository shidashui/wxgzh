# -*- coding: utf-8 -*-
# @Time    : 1/9/2021 10:32 AM
# @Author  : Shui
# @FileName: robot.py
# @Software: PyCharm

from werobot import WeRoBot

myrobot = WeRoBot(enable_session=True,
                  token='spamtest',
                  APP_ID='wx2f798f8e94425837',
                  APP_SECRET='7530d1caffdbcde5be57fbe3bb12b12b')


@myrobot.handler
def hello(message):
    print(message.content)
    return message.content