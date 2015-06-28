# !/usr/bin/env python
# coding: utf-8

l = map(lambda x: x * x, [1, 2, 3, 4, 5])
print l

f = lambda x: x * x
print f

print f(5)

def build(x, y):
    return lambda: x * y + y * y
print build(2, 3)()
