# !/usr/bin/env python
# coding: utf-8

L = [x * x for x in range(10)]
print L

G = (x * x for x in range(10))
print G

for i in G:
    print  i

def fibonacci(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b, n = b, a + b, n + 1

fibonacci(10)

# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b, n = b, a + b, n + 1

# 这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，
# 遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，
# 遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

print fib(10)

for n in fib(10):
    print n

a = 3
b = 5

print (a, b)

(m, n) = (a, b)
print (m, n)

(m, n) = (a, a + b)
print (m, n)

