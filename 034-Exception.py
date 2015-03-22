# !/usr/bin/env python
# coding: utf-8

try:
    print 'try....'
    r = 10 / 0
    print 'result:', r
except ZeroDivisionError, e:
    print 'except:', e
finally:
    print 'finally...'
print 'END'

try:
    print 'try...'
    r = 10 / int('a')
    print 'result: ', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
else:
    print 'no error!'
finally:
    print 'finally...'
print 'END'


import logging

def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e)
main()
print 'END'
