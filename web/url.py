# !/usr/bin/env python
# coding: utf-8

__author__ = 'Moch'

"""
the url structure of website
"""


import sys
reload(sys)
# sys.setdefaultencoding("utf-8")

from handlers.index import IndexHandler
from handlers.user import UserHandler
from handlers.sleep import SleepHandler
from handlers.sleep import SeeHandler

url = [
    (r"/", IndexHandler),
    (r'/user', UserHandler),
    (r'/sleep', UserHandler),
    (r'/see', SeeHandler),
]