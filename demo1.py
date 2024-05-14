import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 打开浏览器
from selenium.webdriver.common.by import By

service = Service(executable_path='D:\deyunce\pythondaima\selenium_40\drivers\chromedriver-win64\chromedriver.exe')
# service = Service(executable_path='drivers/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)


# 最大化浏览器
driver.maximize_window()


# 进入网址（get）
driver.get('https://www.baidu.com')


# 方法1 输入内容      使用该元素等于2大于2用这种
# ------id定位网页元素--------
# sou_suo =driver.find_element(By.ID,'kw')
# print(sou_suo)

# 发送内容
# sou_suo.send_keys('德云测')

# 方法2 写成链式
# driver.find_element(By.ID,'kw').send_keys('德云测')


# 点击
# driver.find_element(By.ID,'su').click()
# time.sleep(3)

# --------link——text定位点击------
# driver.find_element(By.LINK_TEXT,'贴吧').click()
# driver.find_element(By.XPATH,'//a[text()="贴吧"]').click()


# --------模糊点击-------------
driver.find_element(By.PARTIAL_LINK_TEXT,'新').click()
time.sleep(3)




# 关闭浏览器
driver.quit()