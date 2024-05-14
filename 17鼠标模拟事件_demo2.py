import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='D:\deyunce\pythondaima\selenium_40\drivers\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(r'https://www.baidu.com/')
time.sleep(1)

# ========新知识区========
loc_setting = '//span[text()="设置"]'
setting = driver.find_element(By.XPATH, loc_setting)
loc_search_picture_btn = '//span[@class="soutu-btn"]'
search_picture_btn = driver.find_element(By.XPATH, loc_search_picture_btn)

# 链条里面有多个行为
# ActionChains(driver).move_to_element(setting).pause(2).move_to_element(search_picture_btn).pause(2).perform()
ActionChains(driver).move_to_element(setting).pause(2).move_to_element(search_picture_btn).pause(2).perform()
# pause  停顿



# ======================

time.sleep(5)
driver.quit()
