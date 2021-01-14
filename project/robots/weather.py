# -*- coding: utf-8 -*-
# @Time    : 1/14/2021 2:23 PM
# @Author  : Shui
# @FileName: weather.py
# @Software: PyCharm

from pyquery import PyQuery as pq

def get_weather():
    url = 'http://www.weather.com.cn/weather1d/101090101.shtml'
    doc = pq(url=url, encoding='utf-8')

    res = doc('input[id=hidden_title]').attr('value') + '\n' + doc('ul[class=clearfix] li:first p').text().split(' ')[-1]

    return res