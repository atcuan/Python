
# !/usr/bin/env python
# coding: utf-8

# if

age = 22
if age >= 18:
    print 'Your age is ', age
    print 'adult'
else:
    print 'Your age is ', age
    print 'teenager'

age = 3
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
else:
    print 'kid'

# if <条件判断1>:
#     <执行1>
# elif <条件判断2>:
#     <执行2>
# elif <条件判断3>:
#     <执行3>
# else:
#     <执行4>

if age:
    print 'True'


# for...in

names = ['Micheal', 'Lucy', 'Sam']
for name in names:
    print name

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum += x
print sum

print range(10)
sum = 0
for i in range(101):
    sum += i
print sum

sum = 0
n = 99
while n > 0:
    sum += n
    n -= 2
print sum

birth = int(raw_input('birth: '))
if birth < 2000:
    print '00前'
else:
    print '00后'


































