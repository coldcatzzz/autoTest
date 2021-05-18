# import pandas
# import parameterized

# data = pandas.read_excel('calc.xlsx',sheet_name=0,names=['s1','op','s2','yq'],dtype={'s1':str,'op':str,'yq':str},header=None)
# data = data.values.tolist()
# @parameterized.parameterized.expand(data)
# def test(self):
#     print(data)

# test()

# ss = 123
# for i in str(ss):
    # print(i)

# import unittest
# import parameterized

# class Test(unittest.TestCase):
#     @parameterized.parameterized.expand([(1,2,3),(3,4,7),(2,3,5)])
#     def testNumber(self,a,b,c):
#         self.assertEqual(a+b,c)

# if __name__ == '__main__':
#     unittest.main(verbosity=2)

# import unittest
# from parameterized import parameterized   # 引入parameterized模块
# # a = [(1,2,3), (4,5,7)]

# class ceshi(unittest.TestCase):

#     # def test01(self):
#     #     self.assertEqual(2,2)

#     @parameterized.expand([(1,2,3),(4,6,10)])
#     def test02(self,a,b,c):
#         self.assertEqual(a+b,c)


# if __name__=='__main__':
#     unittest.main(verbosity=2)


print([n for n in dir(list) if not n.startswith('_')])










