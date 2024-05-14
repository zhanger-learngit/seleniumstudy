from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

service = Service(executable_path='D:\deyunce\pythondaima\selenium_40\drivers\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get('https://www.baidu.com')
time.sleep(2)

# =========== 新知识区 ============
# class = 类型；class name 类型名称
# aElements = driver.find_elements(By.CLASS_NAME, 'mnav c-font-normal c-color-t')
# 以上代码你发现天衣无缝，但是就是定位不到对象，因为常年来，selenium有个bug
# 如果是通过class_name类型名称定位，如果类型名称是多个单词做成，中间空格隔开，很有可能定位不到，此时，你只需要放第一个单词即可
# 当然，不是100%的，你永远先用全名称，如果不行，记得做我这样的操作
aElements = driver.find_elements(By.CLASS_NAME, 'mnav')
# aElements = driver.find_elements(By.XPATH, '//a[contains(@class, "mnav")]')

for aElement in aElements:
    print(aElement.text)

# ================================

time.sleep(3)
driver.quit()