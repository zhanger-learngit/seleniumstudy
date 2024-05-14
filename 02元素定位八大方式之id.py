from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

service = Service(executable_path='./drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get('https://www.baidu.com')
time.sleep(2)

# =========== 新知识区 ============
# driver.find_element(参数1, 参数2)方法的作用是找到“单个”元素
# 参数1：By.xxx，通过哪种方式寻找元素，By需要导包
# 参数2：元素的定位器（如果通过id方式寻找，那么定位器就是id）
# 返回值：找到的元素对象，拿一个变量名称去接收它
# 如果对象没找到，抛出异常，告诉你，无法找到该对象
souSuoKuang = driver.find_element(By.ID, 'kw')

# 输入框对象下面有一个最常用的方法，叫send_keys()，作用：输入内容
souSuoKuang.send_keys('灌篮高手')
time.sleep(2)
# 下面的写法也可以，我们叫链式写法(一行显示法)（如果这个元素你只操作一次，就用链式写法就OK拉）4
# 按钮框对象有一个最常用的方法，叫click()，作用：左键单击
driver.find_element(By.ID, 'su').click()
time.sleep(2)
# ================================

driver.quit()
