# !/usr/bin/env python
# coding: utf-8

class Animail(object):
    pass

# 大类
class Mammal(Animail):
    pass

class Bird(Animail):
    pass

# 各种动物

class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

class Runnable(object):
    def run(self):
        print 'runing...'

class Flyable(object):
    def fly(self):
        print 'flying...'

class RDog(Mammal, Runnable):
    pass

class FBat(Mammal, Flyable):
    pass
