# !/usr/bin/env python
# coding: utf-8

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print fact(5)
print fact(100)

def fact(n):
    return fact_iter(1, 1, n)
def fact_iter(product, count, max):
    if count > max:
        return product
    return fact_iter(product * count, count + 1, max)
print fact(100)