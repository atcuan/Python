#!/usr/bin/env python
# coding: utf-8

# Character an coding
# UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节
# 常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节


print ord('a')
print ord(u'\u2020')

print u'ABC'.encode('utf-8')
print u'中文'.encode('utf-8')

print len(u'ABC')
print len('ABC')
print len(u'中文')

print 'abc'.decode('utf-8')

print 'Hi, %s, you have $%d.' %('Lucy', 1000)

