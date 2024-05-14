from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

service = Service(executable_path='D:\deyunce\pythondaima\selenium_40\drivers\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(r'file:///D:\deyunce\pythondaima\selenium_40\素材\原生单选框教学素材.html')  # 打开本地的网页文件
# 在字符串前面加一个r，代表用原始状态进行编写字符串，不产生各种特殊效果，比如转义符号
# r = raw = 未加工的
time.sleep(2)

# =========== 新知识区 ============
# 第一关：依次点击每一个明星
# locElements = '//input[@name="star"]'
# elements = driver.find_elements(By.XPATH, locElements)
# # [元素1, 元素2, ..., 元素8]
# for element in elements:
#     element.click()
#     time.sleep(1)

# 第二关：依次点击每一个明星，跳过胡歌和李小龙
# (1)
# //p[text()!="请选择你最喜欢的明星(单选)"]
# //p[not(contains(text(), "最喜欢的明星"))]
# (2) 利用轴定位
# //p[contains(text(), "最喜欢的明星")]/following-sibling::p


pElements = driver.find_elements(By.XPATH, '//p[contains(text(), "最喜欢的明星")]/following-sibling::p')
inputElements = driver.find_elements(By.XPATH, '//input[@name="star"]')
i = 0  # 下标初始值等于0
for pElement in pElements:
    name = pElement.text
    if name in ('胡歌', '李小龙'):
        print(f'{name}没有点击。')
        time.sleep(1)
    else:
        inputElements[i].click()
        time.sleep(1)
    i = i + 1

# ================================

time.sleep(3)
driver.quit()