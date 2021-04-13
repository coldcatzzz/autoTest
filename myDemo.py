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


























































































































































































































































































































































































































































































































































































































































































































