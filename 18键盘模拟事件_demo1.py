import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='D:\deyunce\pythondaima\selenium_40\drivers\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(r'https://www.baidu.com/')
time.sleep(1)

search_box = driver.find_element(By.CSS_SELECTOR,'#kw')
time.sleep(1)
# 点击输入框
ActionChains(driver).click(search_box).perform()
# 键盘输入
# ActionChains(driver).send_keys_to_element(search_box,'德云测').perform()
ActionChains(driver).send_keys_to_element(search_box,'德云测').perform()
time.sleep(1)
# ActionChains(driver).key_down('D').key_up('D').perform()
ActionChains(driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()


# 老师的
# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains, Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service = Service(executable_path='D:\DeyuncePythonStudy\selenium40\drivers\chromedriver.exe')
# driver = webdriver.Chrome(service=service)
# driver.maximize_window()
# driver.get(r'https://www.baidu.com/')
# time.sleep(1)
#
# # ========新知识区========
# search_box = driver.find_element(By.CSS_SELECTOR, '#kw')
#
# ac = ActionChains(driver)
# ac.click(search_box).perform()  # 鼠标左键点击搜索框
# # ac.send_keys_to_element(search_box, '德云测').perform()  # 输入
# ac.key_down('D').key_up('D').perform()
# ac.key_down('Y').key_up('Y').perform()
# ac.key_down('C').key_up('C').perform()
# # 键盘上的按键，需要导入Keys
# ac.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
# # key 键；down 下 => 按下某个键
# # 其实一个链条也可以
# # ActionChains(driver).click(search_box).key_down('D').key_up('D').key_down('Y').key_up('Y').key_down('C').key_up('C').key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
#
#
# # ======================
#
# time.sleep(5)
# driver.quit()
