# 打开浏览器
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='D:\deyunce\pythondaima\selenium_40\drivers\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.maximize_window()

driver.get('https://www.baidu.com')


# --------ID---------
# driver.find_element(By.ID,'kw').send_keys('杨雯淇')
# time.sleep(3)
# driver.find_element(By.ID,'su').click()
# time.sleep(3)

# ---------name---------
# driver.find_element(By.NAME,'wd').send_keys('钢铁侠')
# driver.find_element(By.ID,'su').click()
# time.sleep(3)

# -----------link_text定位点击-----
# driver.find_element(By.LINK_TEXT,'地图').click()
# time.sleep(3)

# ------------partial.link.text 模糊定位--------
# driver.find_element(By.PARTIAL_LINK_TEXT,'新').click()
# time.sleep(3)

# ------------tag_name 通过标签-----------
# aElements = driver.find_elements(By.TAG_NAME, 'a')
# # print(aElements, type(aElements))
# for aElement in aElements:  # 最好的for ... in ... 变量名称写法
#     if len(aElement.text) > 0:
#         # 链接元素的对象下有一个属性叫text，它的作用就是：获取链接显示文字
#         # text属性只能用于，一对标签页中间有文字的
#         print(aElement.text)

# -------------class_name-------
# aElements= driver.find_elements(By.CLASS_NAME,'mnav')
# for aElement in aElements:
#     print(aElement.text)

# ------------XPATH------
driver.find_element(By.XPATH,'//input[@id="kw"]').send_keys('蝙蝠侠')
time.sleep(3)
driver.find_element(By.XPATH,'//input[@id="su"]').click()
time.sleep(3)



driver.quit()