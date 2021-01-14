# -*- coding: utf-8 -*-
# @Time    : 1/9/2021 10:32 AM
# @Author  : Shui
# @FileName: robot.py
# @Software: PyCharm

from werobot import WeRoBot
import re
from .weather import get_weather

myrobot = WeRoBot(enable_session=True,
                  token='spamtest',
                  APP_ID='wx2f798f8e94425837',
                  APP_SECRET='7530d1caffdbcde5be57fbe3bb12b12b')


# @myrobot.handler
# def hello(message):
#     print(message.content)
#     return message.content

# # @robot.text 修饰的 Handler 只处理文本消息
# @myrobot.text
# def echo(message):
#     print('------------内容查看------------')
#     print(message.__dict__)
#     print('content===>',message.content)
#     print('------------结   束------------')
#     return message.content
#
# # @robot.image 修饰的 Handler 只处理图片消息
# @myrobot.image
# def img(message):
#     return message.img

@myrobot.filter(re.compile(".*?天气.*?"), "天气")
def wether(message):
    return get_weather()

