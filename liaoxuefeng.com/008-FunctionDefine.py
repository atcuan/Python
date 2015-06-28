# !/usr/bin/env python
# coding: utf-8

def my_abs(x):
    if not isinstance(x, (int ,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print my_abs(11)

# def nop():
#   pass

import math

def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

r = move(100, 100, 60, math.pi / 6)
# r = move(100, 100, 60)
print r[0], r[1]
