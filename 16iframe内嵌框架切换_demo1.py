import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 打开浏览器
from selenium.webdriver.common.by import By

service = Service(executable_path='D:\deyunce\pythondaima\selenium_40\drivers\chromedriver-win64\chromedriver.exe')
# service = Service(executable_path='drivers/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)


# 最大化浏览器
driver.maximize_window()


# 进入网址（get）
driver.get('http://mail.qq.com')
time.sleep(1)

# 切换两层框架
driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, 'iframe[class="QQMailSdkTool_login_loginBox_qq_iframe"]'))
driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, '#ptlogin_iframe'))


loc_pwd_login ='//a[text()="密码登录"]'
driver.find_element(By.XPATH,loc_pwd_login).click()
loc_account = '#u'
#
driver.find_element(By.CSS_SELECTOR,loc_account).send_keys('2877037162')
time.sleep(1)

# 切回主框架
# driver.switch_to.default_content()
# 切换上一层
# driver.switch_to.parent_frame()

driver.find_element(By.CSS_SELECTOR,'#p').send_keys('zhang..123')

driver.find_element(By.CSS_SELECTOR,'input[value="登录"]').click()
time.sleep(1)

