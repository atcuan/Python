# !/usr/bin/env python
# coding: utf-8

print range(1, 11)

L = []
for x in range(1, 11):
    L.append(x * x)
print L

print [x * x for x in range(1, 11)]

print [m + n for m in 'ABC' for n in 'XYZ']

import os
dirs = [d for d in os.listdir('.')]
print dirs
print len(dirs)

for d in dirs:
    print d

d = {'X': 1, 'Y': 2, 'Z': 3}
for k, v in d.iteritems():
    print k, '=', v

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print [k + '=' + v for k, v in d.iteritems()]

L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]

x = 'abc'
y = 18
print isinstance(x, str)

def myLower(c):
    if isinstance(c, str):
        return c.lower
    return c 

L = ['Hello', 'World', 18, 'IBM', 'Apple']
print [myLower(s) for s in L]

L = ['Hello','World', 18, 'Apple', None]
print [s.lower() for s in L if isinstance(s, str)]

# 高能核器!
print [m.upper() if isinstance(m, str) else m for m in L]

  
