import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='D:\deyunce\pythondaima\selenium_40\drivers\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(r'file:///D:\deyunce\pythondaima\selenium_40\素材\原生弹框教学素材.html')

# ========新知识区========
loc_prompt = 'input[value="我是【提示输入框】类型的弹窗按钮"]'
# prompt 提示
loc_warning = 'input[value="我是【警告提示框】类型的弹窗按钮"]'
# warning 警告
loc_accept = 'input[value="我是【确认框】类型的弹窗按钮"]'
# accept 确认

# 操作提示输入框
# 第一步：先点击并弹出窗口
driver.find_element(By.CSS_SELECTOR, loc_prompt).click()
# 第二步：切入窗口（使用driver.switch_to.alert获得窗口对象）
# alert_object = driver.switch_to.alert
alert_object=driver.switch_to.alert
# 第三步：接下来所有窗口中的操作，都是基于窗口对象的
# 窗口对象的操作一：获取提示词（使用窗口对象的text属性，获取提示词）
print(alert_object.text)

# 窗口对象的操作二：输入内容（自动化有个显示bug，其实输入了，但是实际你是看不到的）
alert_object.send_keys('jczc')
# 窗口对象的操作三：点击【确定】按钮
time.sleep(3)
alert_object.accept()
time.sleep(2)
# accpet 确认、确定的

# 窗口对象的操作四：点击【取消】按钮
driver.find_element(By.CSS_SELECTOR, loc_prompt).click()
time.sleep(2)
alert_object = driver.switch_to.alert
alert_object.dismiss()
# dismiss 取消、驳回
# ======================

time.sleep(5)
driver.quit()

