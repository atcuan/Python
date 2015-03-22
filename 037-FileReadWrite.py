# !/usr/bin/env python
# coding: utf-8

try:
    f = open('/Users/Moch/Github/Python/LICENSE', 'r')
    print f.read()
finally:
    if f:
        f.close()

with open('/Users/Moch/Github/Python/LICENSE', 'r') as f:
    # print f.read()
    for line in f.readlines():
        print line.strip()

with open('/Users/Moch/Github/Python/LICENSE', 'r') as f:
    u = f.read().decode('gbk')
    print u

# 编码
# import codecs

# with codecs.open('/User/Moch/notexistfile', 'r', 'gbk') as f:
    # f.read()

with open('/Users/Moch/Github/Python/PythonIOTestFile', 'w') as f:
    f.write('Hello, world!')
