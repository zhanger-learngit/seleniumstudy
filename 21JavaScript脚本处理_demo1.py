import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service = Service(executable_path='D:\deyunce\pythondaima\selenium_40\drivers\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()


driver.get(r'file:///D:\deyunce\pythondaima\selenium_40\素材\原生隐藏元素js处理教学素材(新版本).html')
time.sleep(1)

# 时间被隐藏不能电脑输入需要更改js脚本
js = 'document.getElementById("deyunce").readOnly=false;'
driver.execute_script(js)

driver.find_element(By.CSS_SELECTOR,'#deyunce').send_keys('2024-02-21')
time.sleep(1)