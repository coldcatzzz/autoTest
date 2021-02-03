from appium import webdriver
from time import sleep

server = 'http://127.0.0.1:4723/wd/hub'
desired_capabilities = {
	'platformName':'Android',
	# 'deviceName':'88Y0219926011315',n
	'deviceName':'192.168.75.101:5555',
	'platformVersion':'9',
	# 'appPackage':'com.android.calculator2',
	# 'appActivity': 'com.android.calculator2.Calculator',
	'noReset':True,
	'appPackage' : 'com.android.quicksearchbox',
	'appActivity' : 'com.android.quicksearchbox.SearchActivity' 
}

driver = webdriver.Remote(server,desired_capabilities)
print('程序开始运行。。。')

driver.find_element_by_id('com.android.quicksearchbox:id/search_src_text').click()
driver.find_element_by_id('com.android.quicksearchbox:id/search_src_text').send_keys('http://www.baidu.com')
driver.press_keycode(66)
sleep(2)
driver.find_element_by_id('org.chromium.webview_shell:id/url_field').clear()
sleep(2)
driver.find_element_by_id('org.chromium.webview_shell:id/url_field').send_keys('http://www.baidu.com')
driver.press_keycode(66)

sleep(3)
driver.quit()
print('well done!')










