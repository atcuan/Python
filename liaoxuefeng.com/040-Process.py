# !/usr/bin/env python
# coding: utf-8

# import os
#
# print 'Process (%s) start...' % os.getpid()
# pid = os.fork()
# if pid == 0 :
#     print 'I am child process (%s) and my parent is %s.' %(os.getpid(), os.getppid())
# else:
#     print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)



# from multiprocessing import Process
# import os
#
# def run_proc(name):
#     print 'Run child process %s (%s)' % (name, os.getpid())

# if __name__ == '__main__':
#     print 'Parent process %s.' % os.getpid()
#     p = Process(target = run_proc, args = ('test', ))
#     print 'Process will start...'
#     p.start()
#     p.join()
#     print 'Process end.'


# from multiprocessing import Pool
# import os, time, random

# def long_time_task(name):
#     print 'Run task %s (%s)...' % (name, os.getpid())
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print 'Task %s run %0.2f seconds.' % (name, (end - start))

# if __name__ == '__main__':
#     print 'Parent process %s.' % os.getpid()
#     p = Pool() # 默认同时跑4个进程
#     for i in range(5):
#         p.apply_async(long_time_task, args = (i, ))
#     print 'Waiting for all subprocess done...'
#     p.close()
#     p.join()
#     print 'All subprocess done.'



from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码
def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())

# 度数据进程的代码
def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value

if __name__ == '__main__':
    q = Queue()
    pw = Process(target = write, args = (q, ))
    pr = Process(target = read, args = (q, ))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()



# 在Unix/Linux下，可以使用fork()调用实现多进程。
# 要实现跨平台的多进程，可以使用multiprocessing模块。
# 进程间通信是通过Queue、Pipes等实现的。

