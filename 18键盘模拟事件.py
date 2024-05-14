import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='./drivers/chromedriver.exe')

dr = webdriver.Chrome(service=service)
dr.maximize_window()
dr.get('https://www.baidu.com')

# ================= 新知识区 ======================
souSuoKuang = dr.find_element(By.XPATH, '//input[@id="kw"]')
ActionChains(dr).send_keys_to_element(souSuoKuang, '德云测').pause(1).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
# send_keys_to_element 模拟键盘，把内容填写到指定的元素对象里
# pause 停顿
# key_down 按下键
# key_up  释放按下的键
time.sleep(2)
# Keys包需要导包，Keys是一个枚举类，里面直接点出各种 键盘上的 键（26个英文字母除外）
# =================================================

# 课堂作业：通过键盘模拟事件的方式在百度搜索框输入YuJie或自己的名字的拼音，每个字的首字母大写
souSuoKuang = dr.find_element(By.XPATH, '//input[@id="kw"]')
ac = ActionChains(dr)
ac.key_down(Keys.LEFT_SHIFT).send_keys_to_element(souSuoKuang, 'y').key_up(Keys.LEFT_SHIFT).perform()  # Y
ac.send_keys_to_element(souSuoKuang, 'u').perform()  # u
ac.key_down(Keys.LEFT_SHIFT).send_keys_to_element(souSuoKuang, 'j').key_up(Keys.LEFT_SHIFT).perform()  # J
ac.send_keys_to_element(souSuoKuang, 'i').perform()  # i
ac.send_keys_to_element(souSuoKuang, 'e').perform()  # e
ac.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()  # 按下回车

time.sleep(2)
dr.quit()