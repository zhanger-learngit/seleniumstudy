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
souSouKuang = driver.find_element(By.NAME, 'wd')
souSouKuang.send_keys('德云测')
time.sleep(2)
souSouKuang.clear()  # 清空搜索框的文本内容
time.sleep(2)
souSouKuang.send_keys('赌不赌？')
# ================================
time.sleep(2)
driver.quit()
