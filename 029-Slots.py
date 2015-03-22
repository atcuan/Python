# !/usr/bin/env python
# coding: utf-8


class Student(object):
    pass

s = Student()
s.name = 'Moch'
print s.name

def set_age(self, age): # 定义一个函数作为实例方法
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s, Student)
s.set_age(24)
print s.age


s2 = Student()
# s2.set_age(22) # Error

# 为了给所有实例都绑定方法，可以给class绑定方法

def set_score(self, score):
    self.score = score

Student.set_score = MethodType(set_score, None, Student)

s.set_score(100)
s2.set_score(99)

print s.score
print s2.score


class SomeClass(object):
    __slots__ = ('name', 'age')

s = SomeClass()
s.name = 'Moch'
s.age = 24
# s.score = 22 # Error

# __slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的





