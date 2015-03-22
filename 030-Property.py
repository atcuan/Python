# !/usr/bin/env python
# coding: utf-8

class Student(object):
    def get_score(self):
        return self.__score
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('Score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('Score must between 0 ~ `00')
        self.__score = value

s = Student()
s.set_score(90)
print s.get_score()

# s.set_score(999)

class SomeClass(object):
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('Score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('Score must between 0 ~ `00')
        self.__score = value

    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

s = SomeClass()
s.score = 60
print s.score
