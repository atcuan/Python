# !/usr/bin/env python
# coding: utf-8

l = [38, 7, 13, 21]
print sorted(l)

def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
print sorted(l, reversed_cmp)


l = ['bob', 'about', 'Zoo', 'Credit']
print sorted(l)

def com_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0

print sorted(l, com_ignore_case)    






