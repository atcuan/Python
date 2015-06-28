# !/usr/bin/env python
# coding: utf-8

# filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素

def is_odd(n):
    return n % 2 == 1

l = [1, 2, 4, 5, 6, 8, 19]    
print filter(is_odd, l)

def not_empty(s):
    return s and s.strip()

l = ['A', ' ', None, 'C', '  ']
print filter(not_empty, l)    

