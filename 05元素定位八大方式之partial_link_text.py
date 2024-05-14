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
# partial = 部分的； partial link text = 部分的链接显示文字（类似数据库的模糊查询）
driver.find_element(By.PARTIAL_LINK_TEXT, '新').click()
# ================================

time.sleep(3)
driver.quit()