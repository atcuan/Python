# !/usr/bin/env python
# coding: utf-8

# dict

names = ['Micheal', 'Lucy', 'Sam']
scores = [99, 45, 89]

d = {'Micheal': 99, 'Lucy': 45, 'Sam': 89}
print d['Micheal']

d['Lucy'] = 89
print d

# erro
# print d['Moch']

print 'Moch' in d
print d.get('Moch')

d['Moch'] = '22' # will append
print d

d.pop('Moch')
print d

# dict 内部存放的顺序和 key 放入的顺序是没有关系的

# 和 list 比较，dict 有以下几个特点：
# 1. 查找和插入的速度极快，不会随着 key 的增加而增加
# 2. 需要占用大量的内存，内存浪费多
#
# 而 list 相反：
# 1. 查找和插入的时间随着元素的增加而增加
# 2. 占用空间小，浪费内存很少
# 
# 所以，dict 是用空间来换取时间的一种方法


## set

s = set([1, 2, 3])
print s

s = set([1, 2, 3, 3, 3, 2])
print s

s.add(7)
s.add(1)
print s

s.remove(2)
print s

# set可以看成数学意义上的无序和无重复元素的集合
# 因此，两个set可以做数学意义上的交集、并集等操作

s1 = set([1, 2, 3])
s2 = set([2, 4, 3])
print s2

print s1 & s2
print s1 | s2

a = ['c', 'b', 'a']
a.sort()
print a

a = 'abc'
print a.replace('a', 'A')
print a








