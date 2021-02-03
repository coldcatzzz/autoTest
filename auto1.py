#encoding = utf-8

from appium import webdriver
import time
import pandas
import unittest

driver = None

class WebApp(unittest.TestCase):
	@classmethod
	def setUpClass(cls):

		server = 'http://127.0.0.1:4723/wd/hub'
		desired_capabilities = {
			'platformName':'Android',
			# 'deviceName':'88Y0219926011315',
			'deviceName':'192.168.75.101:5555',
			'platformVersion':'9',
			'appPackage':'com.android.calculator2',
			'appActivity': 'com.android.calculator2.Calculator',
			'noReset':True,
			# 'appPackage' : 'com.android.quicksearchbox',
			# 'appActivity' : 'com.android.quicksearchbox.SearchActivity' 
		}
		global driver
		driver = webdriver.Remote(server,desired_capabilities)
		print('程序开始运行。。。')

# data = [
# 	['123','+','45','158'],
# 	['23','-','6','17'],
# 	['6','*','8','48']
# ]

# data = []
# file = open('calc.txt','r')
# for x in file:
# 	data.append(x.split())
# file.close()
	def testCalculator2(self):
		global driver
		data = pandas.read_excel('calc.xlsx',sheet_name=0,names=['s1','op','s2','yq'],dtype={'s1':str,'op':str,'yq':str},header=None)
		data = data.values.tolist()
		for i in range(len(data)):
			if data[i][1] == '+':
				data[i][1] = 'add'
			elif data[i][1] == '-':
				data[i][1] = 'sub'
			else:
				data[i][1] = 'mul'
		for i in data:
			for j in range(len(i)-1):
				x = i[j]
				if j != 1:
					for a in str(x):
						driver.find_element_by_id('com.android.calculator2:id/digit_'+a).click()
				else:
					driver.find_element_by_id('com.android.calculator2:id/op_'+i[1]).click()
			driver.find_element_by_id('com.android.calculator2:id/eq').click()
			result = driver.find_element_by_id('com.android.calculator2:id/result').text
			time.sleep(3)
			if result == i[3]:
				print('test ok')
			else:
				print('test bad')



# driver.find_element_by_id('com.android.quicksearchbox:id/search_src_text').send_keys('http://www.baidu.com')
# driver.press_keycode(66)
# time.sleep(3)
# driver.find_element_by_id('org.chromium.webview_shell:id/url_field').clear()
# driver.find_element_by_id('org.chromium.webview_shell:id/url_field').send_keys('http://www.baidu.com')
# driver.press_keycode(66)
# time.sleep(3)
# content = driver.page_source
# assert '用户反馈' in content


	@classmethod
	def tearDownClass(cls):
		# time.sleep(5)
		global driver
		driver.quit()

if __name__ == '__main__':
	unittest.main(verbosity=2)
	print('work well.................')

