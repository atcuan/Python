# !/usr/bin/env python
# coding: utf-8

# def now():
#     print '2015-1-13'
# f = now
# f()

# print now.__name__
# print f.__name__

# import functools
# def log(func):
#     @functools.wraps(func)
#     def warpper(*args, **kw):
#         print 'call %s():' % func.__name__
#         return func(*args, **kw)
#     return warpper

# @log
# def now():
#     print '2015-1-13'
# now()
# print now.__name__


import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wapper(*args, **kw):
            print '%s %s(): ' % (text, func.__name__)
            return func(*args, **kw)
        return wapper
    return decorator

@log('execute')
def now():
    print '2015-1-13'
now()

print now.__name__
