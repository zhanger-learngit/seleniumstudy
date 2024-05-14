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
# tag = 标签；tag name = 标签名称
# driver.find_elements(By.xxx, '定位器')返回的是一个元素列表（多元素定位），
# 如果只有一个元素，它还是一个列表：[新闻]
# 如果是多个我元素，它还是一个列表：[新闻, hao123, 地图][1]
aElements = driver.find_elements(By.TAG_NAME, 'a')
# print(aElements, type(aElements))
for aElement in aElements:  # 最好的for ... in ... 变量名称写法
    if len(aElement.text) > 0:
        # 链接元素的对象下有一个属性叫text，它的作用就是：获取链接显示文字
        # text属性只能用于，一对标签页中间有文字的
        print(aElement.text)


# ================================

time.sleep(3)
driver.quit()