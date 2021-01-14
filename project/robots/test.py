# -*- coding: utf-8 -*-
# @Time    : 1/13/2021 10:16 PM
# @Author  : Shui
# @FileName: test.py
# @Software: PyCharm

from pyquery import PyQuery as pq

url = 'http://www.weather.com.cn/weather1d/101090101.shtml'
doc = pq(url=url,encoding='utf-8')

print(doc('input[id=hidden_title]').attr('value'))
print(doc('ul[class=clearfix] li:first p').text().split(' ')[-1])


