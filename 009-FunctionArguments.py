# !/usr/bin/env python
# coding: utf-8

# def power(x):
# 	return x * x

# print power(5)	

# 默认参数

def power(x, n = 2):	
	s = 1
	while n > 0:
		s *= x
		n -= 1
	return s

print(5)	
print power(5, 3)

def enroll(name, gender, age = 6, city = 'LA'):
	print 'name: ', name
	print 'gender: ', gender
	print 'ae: ', age
	print 'city: ', city

enroll('Sam', 'M')	
enroll('Lucy', 'F', 8)
enroll('Lily', 'F', city = 'Tex')

# 所以，定义默认参数要牢记一点：默认参数必须指向不变对象！

def add_end(L = None):
	if L is None:
		L = []
	L.append('end')
	return L

print add_end
print add_end


# 可变参数
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum += power(n)
	return sum

print calc(1, 2, 3)	

# 在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
nums = [1, 2, 3]
print calc(*nums)


# 关键字参数
print '关键字参数'
def person(name, age, **kw):
	# print 'name: ', name, 'age: ', age, 'others: ', kw
	print 'name: %r, age: %r, others: %r' %(name, age, kw)

print person('Micheal', 30)

print person('Lily', 22, city = 'LA')

# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
kw = {'city': 'Tex', 'job': 'Engineer'}
print person('Jack', '40', **kw)


# 参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数
print '所有参数'
def func(a, b, c = 0, *args, **kw):
	print 'a = ', a, 'b = ', b, 'c = ', c, 'args = ', args, 'kw = ', kw

print func(1, 2)
print func(1, 2, 5)
print func(1, 2, 5, 'dd', 'gg')
print func(1, 2, 5, 'dd', 'gg', x = 99)

# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
args = (1, 2, 3, 5)
kw = {'x': 99}
func(*args, **kw)

# *args是可变参数，args接收的是一个tuple
# **kw是关键字参数，kw接收的是一个dict

# 可变参数既可以直接传入：func(1, 2, 3)
# 又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))

# 关键字参数既可以直接传入：func(a=1, b=2)
# 又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})

