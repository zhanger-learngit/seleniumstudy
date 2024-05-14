import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='D:\deyunce\pythondaima\selenium_40\drivers\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.maximize_window()

driver.get('https://deyunce:828123@mall.deyunce.com/pc/')
time.sleep(1)

driver.find_element(By.XPATH,'//div[@class="sm"]').click()
time.sleep(1)

denglu = '//div[@id="__nuxt"]//div[contains(text(),"账号密码登录")]'
driver.find_element(By.XPATH,denglu).click()
time.sleep(1)

account ='//input[@placeholder="请输入账号/手机号码"]'
driver.find_element(By.XPATH,account).send_keys('17866509585')
time.sleep(1)

password = '//input[@placeholder="请输入密码"]'
driver.find_element(By.XPATH,password).send_keys('123ywq123')
time.sleep(1)

li_ji_denglu ='button[class="el-button el-button--primary"]'
driver.find_elements(By.CSS_SELECTOR,li_ji_denglu)[1].click()
time.sleep(2)

# 点击第二个
#
duihao_list = '//span[@class="el-checkbox__inner"]'
driver.find_elements(By.XPATH,duihao_list)[2].click()
time.sleep(2)


driver.quit()