# !/usr/bin/env python
# coding: utf-8

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print key

for value in d.itervalues():
    print value

for key, value in d.iteritems():
    print key, value 

for ch in 'ABC':
    print ch

from collections import Iterable
print isinstance('abc', Iterable)
print isinstance([1, 2, 3], Iterable)
print isinstance(123, Iterable)

for index, value in enumerate(['A', 'B', 'C']):
    print index, value

for x, y in [(1, 1), (2, 6), (3, 9)]:
    print x, y