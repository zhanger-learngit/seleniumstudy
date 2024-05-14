import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service = Service(executable_path='D:\deyunce\pythondaima\selenium_40\drivers\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(r'file:///D:\deyunce\pythondaima\selenium_40\素材\原生下拉列表复选操作教学素材.html')
time.sleep(1)

# ========新知识区========
select_elem = driver.find_element(By.CSS_SELECTOR, 'select#deyunceSuperStars')
Select(select_elem).select_by_visible_text('胡歌')
time.sleep(1)
Select(select_elem).select_by_visible_text('刘诗诗')
time.sleep(1)
# Select(select_elem).deselect_by_visible_text('胡歌')
Select(select_elem).deselect_all()

# Select(select_elem).deselect_by_index(下标)  根据下标反选
# Select(select_elem).deselect_by_value(选项的value属性的值)  根据value属性的值反选
# Select(select_elem).deselect_by_visible_text(文本显示值)  根据文本显示值反选
# Select(select_elem).deselect_all()  反选所有

# options = Select(select_elem).options
# index = 0
# for opt in options:
#     Select(select_elem).select_by_index(index)
#     index += 1

# # 用于多选框，他会返回所有被选择的选项元素，放入列表，如果需要看值，点出text方法
# print(Select(select_elem).all_selected_options)

# 如果select元素是多选框，返回True，单选的返回False
print(Select(select_elem).is_multiple)

# ======================

time.sleep(5)
driver.quit()
