# !/usr/bin/env python
# coding: utf-8

# class Hello(object):
#     def hello(self, name = 'world'):
#         print 'hello, %s.' % name
# h = Hello()
# print h.hello()

# print type(Hello)
# print type(h)


def fn(self, name = 'world'): # 定义函数
    print 'Hello, %s.' % name

Hello = type('Hello', (object, ), dict(hello = fn)) # 创建 Hello class

h = Hello()
print h.hello()

print type(Hello)
print type(h)

# 要创建一个class对象，type()函数依次传入3个参数：

# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。


# metaclass是创建类，所以必须从`type`类型派生：

class ListMetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
class MyList(list):
    __metaclass__ = ListMetaClass # 指示使用ListMetaclass来定制类

L = MyList()
L.add(1)
print L



class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')
class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Moch':
            return type.__new__(cls, name, bases, attrs)
        mappings = dict()
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                print 'Found mapping: %s ==> %s' % (k, v)
                mappings[k] = v
        for k in mappings.iterkeys():
            attrs.pop(k)
        attrs['__table__'] = name # 假设表名和类名一致
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        return type.__new__(cls, name, bases, attrs)
class Model(dict):
    __metaclass__ = ModelMetaClass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r'"Model" object has no attribute "%s"' % key)
    def __setattr__(self, key, value):
        self[key] = value
    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print 'SQL: %s' % sql
        print 'ARGS: %s' % str(args)

class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：
u.save()

import this
