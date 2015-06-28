# !/usr/bin/env python
# coding: utf-8

import os

print os.name

print os.uname()

print os.environ

for item in os.environ:
    print '%s: %s' % (item, os.getenv(item))

current_path = os.path.abspath('.')
print current_path

# 可以正确处理不同操作系统的路径分隔符
new_dir = os.path.join(current_path, 'testdir')
print new_dir
# os.mkdir(new_dir)

print os.path.split(new_dir)

# os.rename('test.text', 'text.py')
# os.remove('test.py')

print [x for x in os.listdir('.') if os.path.isdir(x)]



def search(key):
    def search_file(path, key):
        for x in os.listdir(path):
            if os.path.isfile(os.path.join(path, x)):
                if os.path.split(x)[1].find(key) != -1:
                    print os.path.join(path, x)
            elif os.path.isdir(os.path.join(path, x)):
                search_file(os.path.join(path, x), key)
            else:
                pass
    search_file(os.path.abspath('.'), key)

print 'Begain search...'
search('LICENSE')
