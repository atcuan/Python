# !/usr/bin/env python
# coding: utf-8


print int('123', base = 8)

def int2(x, base = 2):
    return int(x, base)

print int2('10010')


import functools
int2 = functools.partial(int, base = 2)
print int2('10010')
