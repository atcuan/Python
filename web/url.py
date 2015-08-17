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

url = [
    (r"/", IndexHandler)
]