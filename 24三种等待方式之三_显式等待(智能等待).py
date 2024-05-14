# 当定位某个元素，隐式等待和显式等待同时生效时，听从显式等待（智能等待）
# 等待原理：
# 隐式等待：10秒（所有的元素定位就是最多等10秒）
# 定位A元素，设置了显式等待，等5秒
# 到底A元素等5秒还是10秒？   5秒
# 隐式等待：10秒（所有的元素定位就是最多等10秒）
# 定位B元素，设置了显式等待，等60秒
# 到底B元素等10秒还是60秒？   60秒
# 智能等待的发射检查频率是0.5秒：即：每0.5秒检查（轮询）一次，元素有没有满足EC条件

# 背这些单词
# Service
# webdriver
# webdriver.Chrome()
# By
# ActionChains
# Select
# time
# 以下是显式等待需要背诵的单词
# WebDriverWait(dr浏览器对象, 等待的秒数)
# expected_conditions
# expected_conditions as EC
# EC.visibility_of_element_located(locator定位器)
# 注意：locator定位器的写法必须是一个元组：(By.XPATH, '定位表达式')

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

service = Service(executable_path='./drivers/chromedriver.exe')
dr = webdriver.Chrome(service=service)
dr.implicitly_wait(10)
dr.maximize_window()
dr.get('http://deyunce:828123@hospital.deyunce.com/sel/toLogin')

# 用WebDriverWait的方式定位元素并操作
locatorYongHuMing = (By.CSS_SELECTOR, 'input#loginname')  # 用户名
locatorMiMA = (By.CSS_SELECTOR, 'input#pwd')  # 密码
locatorDengLu = (By.CSS_SELECTOR, 'button[lay-filter="login"]')  # 登录

# 登录

WebDriverWait(dr, 3).until(EC.visibility_of_element_located(locatorYongHuMing), f'{locatorYongHuMing}对象没找到').send_keys('dycadmin')
WebDriverWait(dr, 3).until(EC.visibility_of_element_located(locatorMiMA)).send_keys('123456')
WebDriverWait(dr, 3).until(EC.visibility_of_element_located(locatorDengLu)).click()

time.sleep(2)
dr.quit()

# 智能等待知识总结
# until = 直到
# expected_conditions = 预期的条件
# 最常用的预期条件：
# visibility_of_element_located(元素定位器)：元素可见
# visibility = 可见

# WebDriverWait有2个参数：
# 参数1：你要操控的哪个浏览器驱动对象：dr
# 参数2：智能等待的时间
# 整个WebDriverWait类只有2个方法，util()方法和until_not()方法，但是永远只用until方法
# util方法有2个参数：
# 参数1：传入“预期条件”，EC.visibility_of_element_located()函数
# 作用：智能等待，直到某个元素显示在页面中，才算找到该元素
# 如果最终等到了，那么WebDriverWait实例对象返回该元素，如果没等到，报错：TimeoutException超时异常
# 参数2：可选，可以设置一段一旦超时以后，没定位到元素的，报错信息

# 其他常用EC条件
# （1）
# 找网页框架iframe是否存在，如果在，自动帮你切进去，不用再写dr.switch_to.frame()，
# 如果要切回来，还是要用以下两个的
# dr.switch_to.default_content()
# dr.switch_to.parent_frame()
# WebDriverWait(dr, 3).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//iframe[@id=xxxx]')))
# （2）
# EC.invisibility_of_element_located()  如果不出现了返回True
# invisibility = 不显示
