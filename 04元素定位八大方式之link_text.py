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
# 前端小知识：
# <a>页面显示文字</a> a标签在HTML网页语言里，作用就是“超链接”元素
driver.find_element(By.LINK_TEXT, '新闻').click()
# link = 链接；text = 文本；link text = 链接显示的文本

# ================================

time.sleep(5)
driver.quit()