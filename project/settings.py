# -*- coding: utf-8 -*-
# @Time    : 1/8/2021 10:14 AM
# @Author  : Shui
# @FileName: settings.py
# @Software: PyCharm

import os
import sys

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# print(basedir)

WIN = sys.platform.startswith('win')#区分平台
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'