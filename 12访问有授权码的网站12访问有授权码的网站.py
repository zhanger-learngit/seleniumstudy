import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path='./drivers/chromedriver.exe')
dr = webdriver.Chrome(service=service)
dr.maximize_window()
# 【新知识】有授权码的网站该如何访问？
# 公式：https://授权账号:授权密码@url地址
dr.get('https://deyunce:828123@mall.deyunce.com/pc/')

time.sleep(3)
dr.quit()
