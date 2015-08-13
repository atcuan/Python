#! /usr/bin/env python
# coding: utf-8

__author__ = 'Moch'

L = [1, 2, 3, 4, "Moch."]
print(L)
L.insert(1, "M")
print(L)

def removeItemIfExist(list, item):
    if item in list:
        list.remove(item)
    else:
        print("{} is not in {}".format(item, list))

item = "Moch"
removeItemIfExist(L, item)

def popItemIfExist(list, index):
    if index < len(list):
        return list.pop(index)
    else:
        return None

popedItem = popItemIfExist(L, 5)
print(popedItem)

def swap(lhv, rhv):
    return rhv, lhv

a, b = 1, 2
print("a = {}, b = {}".format(a, b))
a, b = swap(a, b)
print("a = {}, b = {}".format(a, b))

for var in range(10):
    # print(var)
    print var,

print("\n")

for var in range(0, 100, 2):
    print var,

L = [var in range(1, 20, 2)]
print(L)


# 找出100以内的能够被3整除的正整数。
L = [var for var in range(1, 100) if var%3 == 0]
print(L)

name_dict={"name":"qiwsir","lang":"python","website":"qiwsir.github.io"}
for k, v in name_dict.items():
    print("key: {}, value: {}".format(k ,v))


a = [1,2,3,4,5]
b = [9,8,7,6,5]
c = []
for i in range(len(a)):
    c.append(a[i] + b[i])
print(c)

d = []
for x, y in zip(a, b):
    d.append(x+y)
print(d)



class A(object):
    def __getattr__(self, item):
        print("You use __getattr__")
    def __setattr__(self, key, value):
        print("You use __setattr__")
        self.__dict__[key] = value

a = A()
a.x
a.x = 7
print(a.x)


class B(object):
    def __getattribute__(self, item):
        print("You are using __getattribute__")
        return object.__getattribute__(self, item)

b = B()
b.y = 8
print(b.y)

