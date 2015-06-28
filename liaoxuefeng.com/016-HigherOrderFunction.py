# !/usr/bin/env python
# coding: utf-8

print abs(-100)

print abs

fun = abs
print fun(-120)

def add(x, y, f):
    return f(x) + f(y)

print add(3, -8, fun)

