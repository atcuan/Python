# !/usr/bin/env python
# coding: utf-8

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__
    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
    def __call__(self):
        print 'My name is %s.' % self.name

s = Student('Moch')
print s

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n. stop
            a, b = 1, 1
            l = []
            for x in range(stop):
                if x >= start:
                    l.append(a)
                a, b = b, a + b
            return l

for item in Fib():
    print item

f = Fib()
print f[0]

print range(100)[5:10]

print f[2:8]
print s.age()


class Chain(object):
    def __init__(self, path = ''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__
    # def __call__(self, path = ''):
    #     return Chain('%s/%s' % (self._path, path))
    def __call__(self, *args, **kw):
        return Chain('%s/%s' % (self._path, args[0]))
print Chain().status.user.timeline.list
print Chain().users('michael').repos

print s()
print callable(Student('Moch'))
print callable(max)
print callable(None)
print callable('String')
