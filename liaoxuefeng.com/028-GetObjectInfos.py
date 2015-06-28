# !/usr/bin/env python
# coding: utf-8

print type(123)

print type(abs)

print type(123) == type(234)

print type('abc') == type('def')

import types

print type('abc') == types.StringType
print type(u'abc') == types.UnicodeType
print type(str) == types.TypeType
print type(int) == type(str) == types.TypeType

print isinstance('a', (str, unicode))
print isinstance(u'a', (str, unicode))
print isinstance(u'a', basestring)

print 'ABC'.lower()

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

print hasattr(obj, 'x')
print hasattr(obj, 'y')

print setattr(obj, 'y', 19)
print hasattr(obj, 'y')

print getattr(obj, 'y')

print hasattr(obj, 'power')
print getattr(obj, 'power')
fn = getattr(obj, 'power')
print fn()

# l = dir('abc')
# for item in l:
#     print '%s' % item
