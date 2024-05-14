import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='D:\DeyuncePythonStudy\selenium40\drivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(r'https://www.baidu.com/')
time.sleep(1)

# ========新知识区========
loc_setting = '//span[text()="设置"]'
# setting 设置
# ActionChains(driver).move_to_element(loc_setting).perform()

# setting = driver.find_element(By.XPATH, loc_setting)
# ActionChains(driver).move_to_element(setting).perform()

ActionChains(driver).move_to_element(driver.find_element(By.XPATH, loc_setting)).perform()

loc_advanced_search = '//span[text()="高级搜索"]'
# advanced = 高级的；search = 搜索
driver.find_element(By.XPATH, loc_advanced_search).click()

# ActionChains(传入需要操作的浏览器实例对象).行为1.行为n.perform()
# 前面无论你有多少个行为串成一个链条，最后想要生效，一定要写perform()方法，只能写一次
# action = 行为
# chains = 链条
# perform = 执行
# move = 移动
# element = 元素

# ======================

time.sleep(5)
driver.quit()
