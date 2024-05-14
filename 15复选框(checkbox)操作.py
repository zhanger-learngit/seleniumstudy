from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

service = Service(executable_path='D:\deyunce\pythondaima\selenium_40\drivers\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(r'file:///D:\deyunce\pythondaima\selenium_40\素材\原生复选框教学素材.html')  # 打开本地的网页文件
time.sleep(2)

# =========== 新知识区 ============
# duoXuanKuang = driver.find_elements(By.XPATH, '//input[@name="star"]')
# for e in duoXuanKuang:
#     e.click()
#     time.sleep(1)

# 点击张前科
pElements = driver.find_elements(By.XPATH, '//p[contains(text(), "明星")]/following-sibling::p')
inputElements = driver.find_elements(By.XPATH, '//input[@name="star"]')
xiaBiao = 0
for p in pElements:
    if p.text == '张前科':
        inputElements[xiaBiao].click()
        break
    xiaBiao = xiaBiao + 1

# 回家作业：点击所有女明星




# ================================

time.sleep(3)
driver.quit()