# !/usr/bin/env python
# coding: utf-8

# thread是低级模块，threading是高级模块，对thread进行了封装

# import time, threading

# def loop():
#     print 'thread %s is runing...' % threading.current_thread().name
#     n = 0
#     while n < 5:
#         n = n + 1
#         print 'thread %s >>>> %s' % (threading.current_thread().name, n)
#         time.sleep(1)
#     print 'thread %s ended.' % threading.current_thread().name

# print 'thread %s is runing...' % threading.current_thread().name
# t = threading.Thread(target = loop, name = 'LoopThread')
# t.start()
# t.join()
# print 'thread %s ended.' % threading.current_thread().name


import time, threading
balance = 0

def change_it(n):
    # 先存后取，结果应该为0
    global balance
    balance = balance + n
    balance = balance - n
# def run_thread(n):
#     for i in range(100000):
#         change_it(n)

lock = threading.Lock()
def run_thread(n):
    for i in range(100000):
        # 先获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target = run_thread, args = (5, ))
t2 = threading.Thread(target = run_thread, args = (8, ))
t1.start()
t2.start()
t1.join()
t2.join()
print balance


# 多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
# Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。
# 多线程的并发在Python中就是一个美丽的梦。
