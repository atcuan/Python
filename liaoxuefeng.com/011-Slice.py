# !/usr/bin/env python
# coding: utf-8

l = ['Micheal', 'Sarah', 'Tracy', 'Bob', 'Jack']

print l

r = []
n = 3
for i in range(n):
    r.append(l[i])
print r

# Slice
print l[0:3]

print l[:3]

print l[1:3]

print l[-2:-1]

l = range(100)
print l

print l[:10]

print l[-10:]

print l[10:20]

# 前10个数，每两个取一个
print l[:10:2]

# 所有数，每5个取一个
print l[::5]

print l[:]

print (0, 1, 2, 3, 4)[:3]

print 'ABCDEFG'[:3]





