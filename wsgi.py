# -*- coding: utf-8 -*-
# @Time    : 1/14/2021 6:24 PM
# @Author  : Shui
# @FileName: wsgi.py
# @Software: PyCharm

import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from project import app