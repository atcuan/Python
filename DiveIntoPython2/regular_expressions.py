__author__ = 'Moch'

#!/usr/bin/env python
# coding: utf-8

import re

s = '100 BROAD'
r = re.sub('ROAD$', 'RD.', s)
print s

r = re.sub(r'\\bROAD$', 'RD.', s)

r = re.sub(r'\bROAD$', 'RD.', s)
print r

s = '100 BROAD ROAD APT. 3'
r = re.sub(r'\bROAD$', 'RD.', s)
print r

r = re.sub(r'\bROAD\b', 'RD.', s)
print r


import  urllib2

from __future__ import absolute_import