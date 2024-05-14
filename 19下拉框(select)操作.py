from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service = Service(executable_path='D:\deyunce\pythondaima\selenium_40\drivers\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(r'D:\D:\deyunce\pythondaima\selenium_40\素材\原生下拉框教学素材.html')
time.sleep(2)

# =========== 新知识区 ============
# Select类用于处理标签名称是select的网页元素（现在比较少见了）
# select = 选择
# Select类的实例化，需要传入一个webelement网页元素，所以你需要先driver.find_element

selectElem = driver.find_element(By.CSS_SELECTOR, 'select#deyunce')

# =============== 新知识 ===============
# Select(selectElem).select_by_index(1)  # 通过下标进行选择
# Select(selectElem).select_by_value('ming')  # 通过下拉列表中option选项的value属性值进行选择的（要有这个属性才能用）
# Select(selectElem).select_by_visible_text('小明')  # 通过网页上显示的文字进行选择(余老师强推的一种)

# dangQianXuanZe = Select(selectElem).first_selected_option  # 获取当前下拉列表中所选择的选项元素
# # # first 第一个的；select 所选的；option 选项
# if dangQianXuanZe.text == '小明':  # 无法自动点出text，需要手动输入
#     print('选择成功')
# else:
#     print('选择失败')

# 循环打印所有的元素的文本显示值
allOptions = Select(selectElem).options  # 拿所有的这个下拉框里的选项“元素”
for opt in allOptions:
    print(opt.text)
# # ================================



time.sleep(3)
driver.quit()