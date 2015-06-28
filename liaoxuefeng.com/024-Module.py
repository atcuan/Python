# !/usr/bin/env python
# coding: utf-8

' a test module'

__author__ = 'Moch Xiao'

import sys

def test():
    args = sys.argv
    if 1 == len(args):
        print 'hello, world'
    elif 2 == len(args):
        print 'hello, %s!' % args[1]
    else:
        print 'too many arguments'

if __name__ == '__main__':
    test()

try:
    import cStringIO as StringIO
except ImportError: # 导入失败捕获异常
    import StringIO

try:
    import json # python >= 2.6
except ImportError:
    import simplejson as json


def _private_1(name):
    return 'hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)


import sys
print sys.path

for item in sys.path:
    print item
