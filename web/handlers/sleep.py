# !/usr/bin/env python
# coding: utf-8

__author__ = 'Moch'

from base import BaseHandler
import tornado.web
import tornado.ioloop
import time
import tornado.gen

class SleepHandler(BaseHandler):
    # @tornado.web.asynchronous
    # def get(self):
    #     tornado.ioloop.IOLoop.instance().add_timeout(time.time() + 17, callback=self.on_response)
    #
    # def on_response(self):
    #     self.render("sleep.html")
    #     self.finish()

    @tornado.gen.coroutine
    def get(self):
        yield tornado.gen.Task(tornado.ioloop.IOLoop.instance().add_timeout, time.time()+17)
        self.render("sleep.html")

class SeeHandler(BaseHandler):
    def get(self):
        self.render("see.html")