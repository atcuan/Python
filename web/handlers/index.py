# !/usr/bin/env python
# coding: utf-8

__author__ = 'Moch'

import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")