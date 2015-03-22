# !/usr/bin/env python
# coding: utf-8

class Animal(object):
    def run(self):
        print 'animal is runing...'
class Dog(Animal):
    def run(self):
        print 'Dog is runing...'

    def eat(self):
        print 'Eating meat...'

class Cat(Animal):
    def run(self):
        print 'Cat is running...'

dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()

print isinstance(dog, Animal)
print isinstance(dog, Dog)
