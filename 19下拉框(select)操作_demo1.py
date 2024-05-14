import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service = Service(executable_path='D:\deyunce\pythondaima\selenium_40\drivers\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(r'file:///D:\deyunce\pythondaima\selenium_40\素材\原生下拉框教学素材.html')
time.sleep(1)

# ========新知识区========
# Select类是Selenium里专门用于处理select标签的，要导包
# Select(需要操作的select元素)
select_element = driver.find_element(By.CSS_SELECTOR, '#deyunce')
# 操作一：根据选项的下标选择（从0开始）
# Select(select_element).select_by_index(4)
# 操作二：根据选项的value属性选择（前提：要有value属性）
# Select(select_element).select_by_value('ming')
# # 操作三：根据选项的显示文本进行选择
Select(select_element).select_by_visible_text('文君')
# visible = 可见的；text 文本

# 获取当前所选择的选项元素，如果你需要获取这个元素的属性值，需要自己手写.text
current_selected_text = Select(select_element).first_selected_option.text
print(f'当前所选的值是：{current_selected_text}')


# ======================

time.sleep(5)
driver.quit()
