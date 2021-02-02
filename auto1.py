#encoding = utf-8

from appium import webdriver
import time
import os

server = 'http://127.0.0.1:4723/wd/hub'
desired_capabilities = {
	'platformName':'Android',
	# 'deviceName':'88Y0219926011315',
	'deviceName':'192.168.75.101:5555',
	'platformVersion':'9',
	# 'appPackage':'com.puzzle.designisland',
	# 'appActivity': 'com.puzzle.sdk.unity.PZUnityPlayerActivity' 
	'appPackage':'com.android.calculator2',
	'appActivity': 'com.android.calculator2.Calculator',
	'noReset':True,
	# 'appPackage' : 'com.android.quicksearchbox',
	# 'appActivity' : 'com.android.quicksearchbox.SearchActivity' 
}



driver = webdriver.Remote(server,desired_capabilities)
print('程序开始运行。。。')

data = [
	['123','+','45','158'],
	['23','-','6','17'],
	['6','*','8','48']
]

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
			for a in x:
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



time.sleep(5)
driver.quit()

print('work well.................')





 

















