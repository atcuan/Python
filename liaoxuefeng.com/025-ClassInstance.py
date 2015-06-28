# !/usr/bin/env python
# coding: utf-8

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 23)
print bart.name
print bart.score

# 和普通的函数相比，在类中定义的函数只有一点不同，
# 就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。
# 除此之外，类的方法和普通函数没有什么区别，
# 所以，你仍然可以用默认参数、可变参数和关键字参数

bart.print_score()
print bart.get_grade()

