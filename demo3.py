import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='D:\deyunce\pythondaima\selenium_40\drivers\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.maximize_window()

# driver.get('https://www.baidu.com')
# time.sleep(3)
#
# driver.find_element(By.XPATH,'//input[@id="kw"]').send_keys('德云测')
# time.sleep(3)
#
# driver.find_element(By.XPATH,'//input[@id="su"]').click()
# time.sleep(3)

# 打开素材
# driver.get(r'file:///D:\deyunce\pythondaima\selenium_40\素材\原生单选框教学素材-无value.html')

# 循环点击素材里的选项
# loc_radioboxes = 'input[name="star"]'
# radioboxes = driver.find_elements(By.CSS_SELECTOR,loc_radioboxes)
# for radiobox in radioboxes:
#     radiobox.click()
#     time.sleep(0.5)

# 点击单个素材 ！！！ 选择购物车
#
# loc_p_list = '//p[text()!="请选择你最喜欢的明星(单选)"]'
# p_list = driver.find_elements(By.XPATH, loc_p_list)
#
# loc_input_list = '//input[@name="star"]'
# input_list = driver.find_elements(By.XPATH, loc_input_list)
#
# index = 0
#
# for p in p_list:
#     if p.text == '景甜':
#         input_list[index].click()
#         break
#     index = index + 1
# time.sleep(3)
# driver.quit()

driver.get(r'file:///D:\deyunce\pythondaima\selenium_40\素材\原生弹框教学素材.html')
time.sleep(1)

loc_prompt = 'input[value="我是【提示输入框】类型的弹窗按钮"]'
# prompt 提示
loc_warning = 'input[value="我是【警告提示框】类型的弹窗按钮"]'
# warning 警告
loc_accept = 'input[value="我是【确认框】类型的弹窗按钮"]'
# accept 确认


# 操作提示输入框
driver.find_element(By.CSS_SELECTOR, loc_prompt).click()
time.sleep(1)

# 第二步：切入窗口（使用driver.switch_to.alert获得窗口对象）
alert_object = driver.switch_to.alert
time.sleep(1)
# 第三步：接下来所有窗口中的操作，都是基于窗口对象的
# 窗口对象的操作一：获取提示词（使用窗口对象的text属性，获取提示词）
alert_text = alert_object.text
print(alert_text)
# 窗口对象的操作二：输入内容（自动化有个显示bug，其实输入了，但是实际你是看不到的）
alert_object.send_keys('deyunce')

# 窗口对象的操作三：点击【确定】按钮
alert_object.accept()
# accpet 确认、确定的
time.sleep(1)

# 窗口对象的操作四：点击【取消】按钮
driver.find_element(By.CSS_SELECTOR, loc_prompt).click()
time.sleep(2)
alert_object = driver.switch_to.alert
alert_object.dismiss()
time.sleep(1)
# dismiss 取消、驳回