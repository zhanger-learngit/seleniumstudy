from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service = Service(executable_path='./drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
# 案例1
driver.get(r'D:\DeyuncePythonStudy\selenium学习\素材\原生隐藏元素js处理教学素材.html')
# 案例2
# driver.get(r'file:///D:\DeyuncePythonStudy\selenium40\素材\原生隐藏元素js处理教学素材(新版本).html')
time.sleep(2)

# =========== 新知识区 ============
# document指整个html
# getElementById
# getElementByName
# 如果没有id或name，叫开发配合加一下

# 案例1
js = 'document.getElementById("deyunce").style.display="block";'
driver.execute_script(js)  # 执行脚本的方法
time.sleep(2)
# # execute = 执行；script = 脚本；
# time.sleep(3)
Select(driver.find_element(By.XPATH, '//select[@id="deyunce"]')).select_by_visible_text('洋洋')

# # 案例2
# js = 'document.getElementById("deyunce").readOnly=false;'
# driver.execute_script(js)  # 执行脚本的方法
# driver.find_element(By.CSS_SELECTOR, '#deyunce').send_keys('2024-03-01')

# ================================

time.sleep(3)
driver.quit()
