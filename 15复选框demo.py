from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

service = Service(executable_path='D:\deyunce\pythondaima\selenium_40\drivers\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(r'file:///D:\deyunce\pythondaima\selenium_40\素材\原生复选框教学素材.html')  # 打开本地的网页文件
time.sleep(2)

# 不点张前科

# pElements = driver.find_elements(By.XPATH, '//p[contains(text(), "明星")]/following-sibling::p')
# inputElements = driver.find_elements(By.XPATH, '//input[@name="star"]')
# xiaBiao = 0
# for p in pElements:
#     if p.text != '张前科':
#         inputElements[xiaBiao].click()
#     xiaBiao = xiaBiao + 1
#     time.sleep(1)

# 点击女明星
pElements = driver.find_elements(By.XPATH, '//p[text()!="请选择你最喜欢的明星(支持多选)"]')
inputElements = driver.find_elements(By.XPATH, '//input[@name="star"]')
index = 0
for p in pElements:
    if p.text == '唐嫣':
        inputElements[index].click()
    elif p.text == '赵丽颖':
        inputElements[index].click()
    elif p.text == '景甜':
        inputElements[index].click()
    elif p.text == '杨幂':
        inputElements[index].click()
    index = index + 1
    time.sleep(1)