from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service = Service(executable_path='./drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(r'D:\DeyuncePythonStudy\selenium学习\素材\原生下拉列表复选操作教学素材.html')
time.sleep(2)

# =========== 新知识区 ============
duoXuanXiaLaKuang = driver.find_element(By.XPATH, '//select[@id="deyunceSuperStars"]')
Select(duoXuanXiaLaKuang).select_by_visible_text('刘亦菲')
time.sleep(1)
Select(duoXuanXiaLaKuang).select_by_visible_text('黄渤')
time.sleep(1)

# Select(duoXuanXiaLaKuang).deselect_by_visible_text('刘亦菲')
# time.sleep(1)
# Select(duoXuanXiaLaKuang).deselect_by_visible_text('黄渤')
# # deselect系列是反选的作用，最常见的是deselect_by_visible_text
#
# Select(duoXuanXiaLaKuang).deselect_all()  # 反选全部

# 作为多选的一种自动验证
suoYouXuanZeDeYuanSu = Select(duoXuanXiaLaKuang).all_selected_options  # 返回当前所有选择的选项元素

count = 0
for yuanSu in suoYouXuanZeDeYuanSu:
    # print(yuanSu.text)  # 打印一下所有被选择的元素
    if yuanSu.text in ('刘亦菲', '黄渤'):
        count = count + 1
if count == 2:
    print('验证刘亦菲和黄渤被选择：Passed')
else:
    print('验证刘亦菲和黄渤被选择：Failed')

# ================================

time.sleep(3)
driver.quit()