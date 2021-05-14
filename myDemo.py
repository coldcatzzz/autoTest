#取列表最大值(1)
# numbers = [2, 2, 3, 4, 5, 99, 7, 8, 9, 10]
# max = 0
# for ss in numbers:
#     if ss > max:
#         max = ss
# print(max)

#取列表最大值(2)
# numbers = [2, 2, 666, 4, 5, 99, 7, 8, 9, 10]
# max = numbers[0]
# for ss in numbers:
#     if ss >= max:
#         max = ss
# print(max)


#取列表最小值
# numbers = [2, 2, 3, 4, 5, 99, 7, 1, 9, 10]
# min = numbers[0]
# for ss in numbers:
#     if ss <= numbers[0]:
#         min = ss
# print(min)

#计算列表的长度
# numbers = [1, 2, 3, 4, 5, 99, 7, 8, 9, 10]
# length = 0
# for ss in numbers:
#     length += 1
# print(length)

# numbers = [1,5]
# numbers[1:2:10] = [2]
# print(numbers)

#常规复制只是将另一个名称关联到列表
# a = [1,2,3]
# b = a
# b[1] = 99
# print(a)

#要让a和b指向不同的列表，就必须将b关联到a的副本
# a = [1,2,3]
# b = a.copy()
# print(b)
# b[1] = 999
# print(b)
# print(a)

#统计次数
# x = [[1, 2], 1, 1, [2, 1, [1, 2]]]
# ss = x[:-1].count([1,2])   #用x[2]不行
# print(ss)

#附加多个元素
# a = [1,2,3]
# b = [4,5,6]
# a.extend(b)
# print(a)

#附加一个元素
# a = [1,2,3]
# b = [4,5,6]
# a.append(b)
# print(a)    #[1, 2, 3, [4, 5, 6]]

#加号拼接使用的是a和b的副本，效率低于extend
# a = [1,2,3]
# b = [4,5,6]
# print(a+b)
# print(a) #[1,2,3]

#使用切片模仿extend
# a = [1,2,3]
# b = [4,5,6]
# a[len(a):] = b
# print(a)

#插入数据
# a = [1,2,3,5,6,7]
# a.insert(3,[4])
# print(a)
# b = a
# b[3:3] = [4]
# print(b)

#删除尾数据
# a = [1,2,3]
# a.append(a.pop())
# print(a) #[1,2,3]

#删除指定值
# a = [1,2,3]
# a.remove(2) #使用remove([2])报错
# print(a)

#列表反转
# a = [1,2,3]
# a.reverse()
# print(a)

# b = [1,2,3]
# print(list(reversed(b)))

#排序
# a = [1,4,2,5,3,6,3,9,2]
# a.sort()
# print(a)

#因为sort()不返回值，报错
# b = [1,4,2,5,3,6,3,9,2]
# y = x.sort()
# print(y)

#使用sorted()排序
# a = [1,4,2,5,3,6,3,9,2]
# b = sorted(a)
# print(b)

# ss = 'helly'
# print(ss[0:3])

# fullname = ['Mike','Scofield']

# print('Mr {name[1]}'.format(name = fullname))

# print('the number {num} is {num:b}'.format(num = 99))

# ss = '{num:10}'.format(num = 3)
# aa = '{name:10}'.format(name = 'cat')   
# print(ss)
# print(aa,',','len = ',len(aa))

#多个{}{}的时候，需要指定位置,0,1,2
# from math import pi
# ss = 'PI is {:.2f}'.format(pi)
# print(ss)

# ss = '{0:010.2f}\n{0:010.3f}'.format(pi)
# print(ss)

# ss = '{0:<10.2f}\n{0:^10.2f}\n{0:>10.2f}'.format(pi)
# print(ss)

# aa = '{:*^50}'.format(' big win ')
# print(aa)

# aa = '{0:10.2f}\n{1:=10.2f}'.format(pi,-pi)
# print(aa)

# aa = '{0:-.2}\n{1:-.2}'.format(pi,-pi)

# bb = '{0:+.2}\n{1:+.2}'.format(pi,-pi)

# cc = '{0: .2}\n{1: .2}'.format(pi,-pi)

# print(aa)
# print(bb)
# print(cc)

# ss = '{0:+10}\n{1:+}'.format(66,33)
# print(ss)

#按照设定格式显示商品价格
# width = int(input('Please enter width: '))
# price_width = 10
# item_width = width - price_width
# header_fmt = '{{:{}}}{{:>{}}}'.format(item_width, price_width) # 40 10
# fmt = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)
# print('=' * width)
# print(header_fmt.format('Item','Price'))
# print('-' * width)
# print(fmt.format('Apples', 0.4))
# print(fmt.format('Pears', 0.5))
# print(fmt.format('Cantaloupes', 1.92))
# print(fmt.format('Dried Apricots (16 oz.)', 8))
# print(fmt.format('Prunes (4 lbs.)', 12))
# print('=' * width)

# print(header_fmt)  #{:40}{:>10}

#字符串居中
# print('pzx'.center(20,'*'))

#查找子串
# title = 'I like python'
# ss = title.find('like')
# print(ss)  # 2
# ss2 = title.find('zzz')
# print(ss2)  # -1

#合并字符串
# s1 = ['1','2','3','4','5']
# s2 = '+'
# print(s2.join(s1))

# dirs = '','usr','bin','env'
# print('/'.join(dirs))
# print('C:' + '\\'.join(dirs))

# ss = ['Aa','bb','cc']
# aa = 'aa'
# for i in ss:
#     if aa == i.lower():
#         print('okk')
#         break
#     else:
#         print('no')

#字符串替换
# ss = 'this is a test'.replace('a','MY')
# print(ss)

#字符串分割
# ss = '1+2+3+4+5'.split('+')
# print(ss)  # ['1', '2', '3', '4', '5']

# ss2 = '/usr/bin/env'.split('/')
# print(ss2)  # ['', 'usr', 'bin', 'env']

# ss3 = 'i like python'.split()
# print(ss3)  # ['i', 'like', 'python']

# 去除字符串首尾空白
# names = ['abc','def','ghj']
# name = ' abc ' # 多空格
# if name.strip() in names:
#     print('ok')

# ss = '***I *** like **** python'.strip('*')
# print(ss)  # I *** like **** python

#单字符转换 translate
#使用translate前要先创建一个转换表
# table = str.maketrans('cs','kz') #对应位置转换
# st = 'this is an incredible test'.translate(table)
# print(st)  # thiz iz an inkredible tezt
# table2 = str.maketrans('cs','kz',' ')
# st = 'this is an incredible test'.translate(table2)
# print(st)  # thizizaninkredibletezt

# ss = '6'
# print(ss.isdigit())  # True

#创建字典
# items = [('name','Tom'),('age',20)]
# d = dict(items)
# print(d)

# dd = dict(name = 'Tom',age = 20)
# print(dd)

# ss = {'name':'Tom','sex':'man'}
# print(ss)

# s = []
# s[1] = 'tomy'
# print(s) #  list assignment index out of range

# s = {}
# s[22] = 'tmo'
# print(s)

# people = {
#     'Alice': {
#         'phone': '2341',
#         'addr': 'Foo drive 23'
#     },
#     'Beth': {
#         'phone': '9102',
#         'addr': 'Bar street 42'
#     },
#     'Cecil': {
#         'phone': '3158',
#         'addr': 'Baz avenue 90'
#     }
# }

# labels = {
#     'phone': 'phone number',
#     'addr': 'address'
# }
# name = input('Name: ')
# request = input('Phone number (p) or address (a)? ')
# if request == 'p': key = 'phone'
# if request == 'a': key = 'addr'
# if name in people: print("{}'s {} is {}.".format(name, labels[key], people[name][key]))

# template = '''<html>
#                 <head><title>{title}</title></head>
#                 <body>
#                 <h1>{title}</h1>
#                 <p>{text}</p>
#                 </body>
#                 </html>
#             '''

# data = {'title': 'My Home Page', 'text': 'Welcome to my home page!'}
# print(template.format_map(data))

#停车游戏
# commend = ''
# started = False
# while True:
#     commend = input('> ')
#     if commend == 'start':
#         if started:
#             print('car is already started!')
#         else:
#             started = True
#             print('car start...')
#     elif commend == 'stop':
#         if not started:
#             print('car is already stopped')
#         else:
#             started = False
#             print('car stop')
#     elif commend =='help':
#         print('''
#             start - to start the car
#             stop - to stop the car
#             quit - to exit
#         ''')
#     elif commend == 'quit':
#         break
#     else:
#         print("I dont't understand")

# price = [10,20,30]
# sum = 0
# for i in price:
#     sum += i
# print(f'sum is {sum} dollers')

# for x in range(4):
#     for y in range(3):
#         print(f'({x},{y})')

# numbers = [5,2,5,2,2]
# for count in numbers:
#     outLook = ''
#     for xx in range(count):
#         outLook += 'x'
#     print(outLook)

# numbers = [2,3,56,7,3,2,2,5,2,1]
# max = 0
# for each in numbers:
#     if each >= max:
#         max = each
# print(max)

# num1 = [1,2,3,2,6]
# num2 = num1.copy()
# num2.remove(3)
# print(num1)
# print(num2)

# numbers = [2,2,3,3,6,6,4,1,8,7,7,6,4]
# other = []
# for number in numbers:
#     if number not in other:
#         other.append(number)
# print(other)

# nums = (1,2,3)
# x,y,z = nums
# print(x,y)

# dict_test = {
#     '1':'one',
#     '2':'two',
#     '3':'three'
# }
# result = input('your phone:') 
# for x in result:
#     print(dict_test[x],' ',end='')  

# def greet_user(first_name,last_name):
#     print(f'Hi, {first_name} {last_name}')

# greet_user('Ma',last_name= 'Jack')

# def square(num):
#     return num * num

# print(square(10))

# def get_emoji(face):
#     words = face.split(' ') # good morning :)
#     emojis = {
#         ':)' : '"smile"',
#         ':(' : '"cry"'
#     }

#     output = ''
#     for word in words:
#         output += emojis.get(word,word) + ' '
#     return output

# msg = input('> ')
# print(get_emoji(msg))

# try:
#     age = int(input('age:'))
#     income = 20000
#     risk = income/age
#     print(age)
#     print(risk)
# except ZeroDivisionError:
#     print('age cannot be zero')
# except ValueError:
#     print('Invalid value')

# class Point():

#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def move(self):
#         print('move')

#     def draw(self):
#         print('draw')

# try:
#     point = Point(10,20)
#     print(point.x)
#     print(point.y)
#     print(point.z)
# except AttributeError:
#     print('wrong value')

# class Person:
#     def __init__(self,name):
#         self.name = name

#     def talk(self):
#         print(f'Hi,I am {self.name}')

# tom = Person('tom')
# tom.talk()
# print(tom.name)
# bob = Person('bob')
# bob.talk()

# class Mammal():
#     def walk(self):
#         print('walk...')


# class Dog(Mammal):
#     ...


# class Cat(Mammal):
#     ...


# d1 = Dog()
# d1.walk()

# c1 = Cat()
# c1.walk()

# from utils import find_max

# result = find_max([1,2,5,7,34,7,3,6,6,445])
# print(result)

# import random
# list_random = []
# for i in range(5):
#     # print('{:.3f}'.format(random.random()))
#     result = random.randint(1,6)
#     list_random.append(result)
#     print(result)
# list_random.sort()
# print(list_random)

# members = ['tom','jack','black','mike']

# leader = random.choice(members)
# print(leader.title())

# import random

# class Dice():
    
#     def roll(self):
#         first = random.randint(1,6)
#         second = random.randint(1,6)
#         return first , second 

# dice = Dice()
# print(dice.roll())

#添加文件夹，删除文件夹
# from pathlib import Path

# path = Path()
# # if path.exists() == False:
# #     path.mkdir()
# for file_list in path.glob('*'):
#     print(file_list)

#execl
# import openpyxl as xl
# from openpyxl.chart import BarChart , Reference

# def process_workbook(filaname):
#     wb = xl.load_workbook(filaname)
#     sheet = wb['Sheet1']
#     sheet['d1'] = 'correct_price'

#     for row in range(2,sheet.max_row +1):  # 2,5
#         cell = sheet.cell(row , 3)
#         correct_price = cell.value * 0.9
#         correct_price_cell = sheet.cell(row,4)
#         correct_price_cell.value = correct_price

#     values = Reference(sheet,
#                         min_row=2,
#                         max_row=sheet.max_row,
#                         min_col=4,
#                         max_col=4
#     )

#     chart = BarChart()
#     chart.add_data(values)
#     sheet.add_chart(chart,'b6')

#     wb.save(filaname)

# process_workbook('transactions.xlsx')

# def febs(num): #形参
#     result = [0 , 1]
#     for i in range(num-2):
#         result.append(result[-2] + result[-1])
#     return result

# print(febs(10)) #实参


# num = 1
# def fun1():
#     global num
#     print(num)
#     num = 123
#     print(num)
# fun1()
# print(num)

# ss = {'name':'zzz'}
# print(ss['name'])

# def pa(**params):
#     print(params)

# pa(x=1,y=2,z=3)

# def add(x,y):
#     return x + y

# params = (1,2)
# print(add(*params))

# def hello_3(greeting='Hello', name='world'):
#     print('{}, {}!'.format(greeting, name))

# params = {'name':'ppp','greeting':'sz'}
# hello_3(**params)

# def power(x, y, *others):
#     if others:
#         print('Received redundant parameters:', others)
#     return pow(x, y)

# # print(power(y=5,x=2))
# params = (5,) * 2
# print(params)   #(5,5)
# print(power(*params))   #?        3125
# print(5**5)

# x = 1
# scope = vars()
# print(scope['x'])
# scope['x'] += 1
# print(x)

# def foo():
#     x = 22
#     x = 33
#     x = 55

# x = 1
# foo()
# print(x)

# def output(x):
#     print('x =',x)

# x = 1
# y = 2
# output(y)

# external = 'berry'
# parameter = 'jack'

# def combine(parameter):
#     global external
#     print(parameter , globals()['parameter'])

# combine('shrub')

# y = 1
# def sum(x):
#     global y
#     y = 2
#     return x + y

# print(sum(2))

# x = 1
# def change():
#     global x
#     x += 1

# change()
# print(x)

# def multiplier(factory):
#     def multiplyByFactory(number):
#         return number * factory
#     return multiplyByFactory

# double = multiplier(2)  
# print(double(5))

# print(multiplier(5)(4))

# def x():
#     return x()

# print(x())

# x = 1
# while True:
#     x+=1
#     print(x)


# while True:
#     x = 1
#     x+=1
#     print(x)

# def factorial(n):
#     result = n
#     for i in range(1,n):
#         result *= i
#     return result

# print(factorial(5))

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(3))

# def power(x,n): # 2**3
#     result = 1
#     for i in range(n):
#         result *= x
#     return result

# def power2(x,n):
#     if n == 0:
#         return 1
#     else:
#         return x * power2(x, n-1)

# print(power2(2, 3))

# seq = [1,2,3,4]
# seq.sort()

# def search(sequence,number,lower = 0,upper = None):
#     if upper == None:
#         upper = len(sequence) - 1
#     if lower == upper:
#         assert number == sequence[upper]
#         return upper
#     else:
#         middle = (lower + upper ) //2
#         if number > sequence[middle]:
#             return search(sequence, number,middle+1,upper)
#         else:
#             return search(sequence, number,lower,middle)

# print(search(seq , 2))

# print(seq.index(3))

# arr = [1,2,3,4,5,6,7,8]

# num = 4
# count = 0
# for i in arr:
#     if i != num:
#         count += 1
#     else:
#         print('num的下标是:',count)

# seq = ["foo", "x41", "?!", "***"]

# re = filter(lambda x : x.isalnum(), seq)
# ss = filter(lambda x : x.isalnum(), seq)
# print(ss)

# ss = [x for x in seq if x.isalnum()]
# print(ss)

# ss = [str(i) for i in range(10)]
# print(ss)

# s1 = list(map(str,range(10)))
# print(s1)

# from functools import reduce
# numbers = []
# for i in range(101):
#     if i != 0:
#         numbers.append(i)
        
# print(numbers)
# print(sum(numbers))
# print(reduce(lambda x , y : x + y, numbers))

# from random import choice

# s1 = choice([1,2,3,4,5,6])
# s2 = choice([1,2,3,4,5,6])
# s3 = choice([1,2,3,4,5,6])
# s4 = choice([1,2,3,4,5,6])
# s5 = choice([1,2,3,4,5,6])
# s6 = choice([1,2,3,4,5,6])
# print(s1,s2,s3,s4,s5,s6)

# def lenth_msg(x):
#     print('the length of' , repr(x) , 'is' ,len(x))

# lenth_msg([1,2,3])

# class Person:
    
#     def set_name(self,name):
#         self.name = name

#     def get_name(self):
#         return self.name

#     def greet(self):
#         print("hello,world! I'm {}.".format(self.name))

# p = Person()
# p.set_name('Jack')
# print(p.get_name())
# p.greet()
# print(p.name)

# p2 = Person()
# p2.name = 'Tom'
# p2.greet()

# class Class():

#     method = ''

#     def method(self):
#         print('i have self')

# def function():
#     print('i dont')

# ins = Class()
# ins.method()

# ins.method = function
# ins.method()

# class Bird:
#     song = 'squaawk'
    
#     def sing(self):
#         print(self.song) 

# bird = Bird()
# bird.sing()
# birdsong = bird.sing
# birdsong()

# class Secretive:

#     name = 'test1'
#     __age = 25

#     def __inaccessible(self):
#         print('you cant see me')

#     def sccessible(self):
#         print('the secret message is :')
#         self.__inaccessible()

# s = Secretive()
# # s.__inaccessible()
# s.sccessible()
# s._Secretive__inaccessible()

# print(s.name)
# s.name = 'test2'
# print(s.name)
# print(s._Secretive__age)
# s._Secretive__age = 30
# print(s._Secretive__age)

# class MemberCounter:
#     count = 0
#     def init(self):
#         MemberCounter.count += 1

# m1 = MemberCounter()
# m1.init()
# print(m1.count)

# m2 = MemberCounter()
# m2.init()
# print(m2.count)


# m1.count = 100
# print(m1.count)

# print(m2.count)

# class Filter:
#     def init(self):
#         self.blocked = []
#     def filter(self , sequence):
#         return [x for x in sequence if str(x).lower() not in self.blocked]

# class SPAMFilter(Filter):
#     def init(self):
#         self.blocked = ['spam']

# f = Filter()
# f.init()
# re = f.filter([1,2,3])
# print(re)

# s = SPAMFilter()
# s.init()
# re = s.filter(['spam', 'SpAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM']) # ['eggs', 'bacon']
# print(re)

# class ABCFilter(Filter):
#     def init(self):
#         self.blocked = ['abc']

# abc = ABCFilter()
# abc.init()
# re = abc.filter(['ab','bc','ac','abc','ABC','abcd','eee'])
# print(re)

# class Animal:
#     pass

# class Bird(Animal):
#     pass

# print(issubclass(Bird, Animal))
# print(issubclass(Animal, Bird))

# print(Bird.__bases__)
# print(Animal.__bases__)
# print(object.__bases__) # None

# b1 = Bird()
# print(isinstance(b1, Bird))
# print(isinstance(b1, Animal))

# print(b1.__class__())

# a1 = Animal()
# print(a1.__class__())

# print(type(b1))
# print(type(a1))

# 计算器
# class Calculator:
#     def calculate(self,expression):
#         self.value = eval(expression)

#     def talk(self):
#         print('cal value is :',self.value)

# class Talker:
#     def talk(self):
#         print('value:',self.value)

# class TalkingCalculator(Talker,Calculator):
#     ...

# tc = TalkingCalculator()
# tc.calculate('1+2+3')
# print(tc.value)
# print(type(tc.value)) # int
# tc.talk()

# #检查属性是否存在
# print(hasattr(tc, 'talk'))
# print(hasattr(tc, 'aaa'))

# #检查属性是否可以调用
# print(callable(getattr(tc,'talk',None)))
# print(callable(getattr(tc,'aaa',None)))

#抽象类
# from abc import ABC , abstractmethod

# class Talker(ABC):
#     @abstractmethod #子类必须实现所有的基类抽象方法
#     def talk(self):
#         pass

#     @abstractmethod    
#     def run(self):
#         pass

# # t = Talker() # 报错，抽象类不能实例化

# class Knigget(Talker):
#     def talk(self):
#         print('Hi')

#     def run(self):
#         print('running')

# class Runner(Talker):
#     def run(self):
#         print('running')

#     def talk(self):
#         print('talking...')

# k = Knigget() #报错，还没有实现基类的方法，无法实例化

# k = Knigget()
# print(isinstance(k, Knigget)) #True
# print(isinstance(k, Talker))
# k.talk()
# k.run()

# r = Runner()
# print(isinstance(r, Runner))
# r.run()
# r.talk()

# # 鸭子类型
# class Herring:
#     def talk(self):
#         print('Bulb.')

# h = Herring()
# print(isinstance(h, Talker))
# print(type(h))

# Talker.register(Herring)
# print(isinstance(h, Talker))
# h.talk()

# class Clam:
#     pass

# Talker.register(Clam)
# print(issubclass(Clam, Talker))

# c = Clam()
# print(isinstance(c, Talker))
# # c.talk() # x 

#异常
# try:
#     x = int(input('first:'))
#     y = int(input('second:'))
#     print(x/y)
# except ZeroDivisionError:
#     print("The second number can't be zero!")
# except ValueError: # not TypeError
#     print("That wasn't a number, was it?")

# 捕获多个异常
# try:
#     x = int(input('first:'))
#     y = int(input('second:'))
#     print(x/y)
# except (ValueError , TypeError , ValueError , NameError , ZeroDivisionError):
#     print('please enter right number')

# try:
#     x = int(input('first:'))
#     y = int(input('second:'))
#     print(x/y)
# except (ZeroDivisionError , ValueError) as e:
#     print(e)

# try:
#     x = int(input('first:'))
#     y = int(input('second:'))
#     print(x/y)
# except:
#     print('womething wrong happened')

# class MuffledCalculator:
#     muffled = False
#     def calc(self,expr):
#         try:
#             return eval(expr)
#         except ZeroDivisionError:
#             if self.muffled:
#                 print('Division by zero is illegal')
#             else:
#                 raise

# calculator = MuffledCalculator()
# # print(calculator.calc('10/2'))
# print(calculator.calc('10/0'))

# try:
#     1/0
# except ZeroDivisionError:
#     raise ValueError from None

# try:
#     print('a task')
# except:
#     print('some wrong')
# else:
#     print('ok')

# while True:
#     try:
#         x = int(input('first:'))
#         y = int(input('second:'))
#         print(x/y)
#     except:
#         print('womething wrong happened')
#     else:
#         break

# while True:
#     try:
#         x = int(input('first:'))
#         y = int(input('second:'))
#         print(x/y)
#     except Exception as e:
#         print('Invalid input:',e)
#         print('try again')
#     else:
#         break

# x = None
# try:
#     1/0
# finally:
#     print('clean...')
#     del x

try:
    1/1
except ZeroDivisionError:
    print('Unknow variable')
else:
    print('That went well')
finally:
    print('Clean...')






























