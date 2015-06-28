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


# import functools
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wapper(*args, **kw):
#             print '%s %s(): ' % (text, func.__name__)
#             return func(*args, **kw)
#         return wapper
#     return decorator
#
# @log('execute')
# def now():
#     print '2015-1-13'
# now()
#
# print now.__name__

import functools
import time

def log(textOrFunc):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if isinstance(textOrFunc, str):
                print("%s begin call %s():" % (textOrFunc, func.__name__))
            else:
                print('begin call %s()' % func.__name__)
            result = func(*args, **kw)
            print('end call %s' % func.__name__)
            return result
        return wrapper
    if isinstance(textOrFunc, str):
        return decorator
    else:
        return decorator(textOrFunc)

# @log
@log('test')
def now():
    print time.strftime('%Y-%m-%d')

now()
