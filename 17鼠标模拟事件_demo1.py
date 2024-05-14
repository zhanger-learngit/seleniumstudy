import time

from selenium import webdriver
from selenium.webdriver import ActionChains
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
time.sleep(1)

# ActionChains(浏览器实例对象driver).move_to_element(元素对象)  鼠标移动到指定的元素

# 鼠标移动到设置
# # action 行为 chain链条 需要导包 (括号里加浏览器实例对象drive)＋行为() + perform()
ActionChains(driver).move_to_element(driver.find_element(By.XPATH,'//span[text()="设置"]')).perform()
time.sleep(1)
#
# # 高级搜索
driver.find_element(By.XPATH,'//span[text()="高级搜索"]').click()
time.sleep(1)







