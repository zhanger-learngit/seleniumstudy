from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

service = Service(executable_path='./drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get('https://www.baidu.com')
time.sleep(2)

# =========== 新知识区 ============
# ~ 案例1 ~
# (1) 获取句柄列表
# 刚开打百度首页的时候获取句柄列表，此时有1个
window_handles_list = driver.window_handles
print(window_handles_list)

loc_news = '//a[text()="新闻"]'
loc_support_mode = 'li[data-text="辅助模式"]'
loc_out_of_service = 'i[title="退出服务Ctrl+Alt+E"]'

# 点新闻，会打开新的窗口
driver.find_element(By.XPATH, loc_news).click()
time.sleep(3)
# 再次获取句柄列表，此时有2个
window_handles_list = driver.window_handles
print(window_handles_list)
# 获取当前的句柄编号，发现其实依然是在老窗口
current_handle = driver.current_window_handle
print(f'当前所激活的窗口的句柄号：{current_handle}')
# 切换句柄
# 如何获取新打开的窗口的句柄号？
# 第一步：使用下标-1获取句柄列表的最新的那个
new_window_handle = window_handles_list[-1]
# 第二步：根据新的句柄编号进行切换
driver.switch_to.window(new_window_handle)
# 切换句柄以后，再次获取当前的句柄编号，发现当前的句柄编号已经是新窗口（代表：切换窗口成功）
current_handle = driver.current_window_handle
print(f'切换后，当前所激活的窗口的句柄号：{current_handle}')

# 点辅助模式
driver.find_element(By.CSS_SELECTOR, loc_support_mode).click()
time.sleep(2)
# 退出服务
driver.find_element(By.CSS_SELECTOR, loc_out_of_service).click()
time.sleep(2)

# 切回老窗口继续操作页面上的元素
# 第一步：关闭当前激活的窗口
driver.close()
time.sleep(2)
# 第二步：把句柄重新切回老窗口（句柄列表的第0个元素）
old_window_handle = window_handles_list[0]
# 第三步：使用句柄编号切换窗口
driver.switch_to.window(old_window_handle)
# 第四步：回到老窗口以后，继续操作老窗口上的页面元素
driver.find_element(By.CSS_SELECTOR, '#kw').send_keys('德云测')
# ================================

# # =========== 新知识区 ============
# # ~ 案例2 ~
# # 每一个窗口都有一个随机生成的id号（专业：句柄）
#
# # 在图片里搜索 德云社
# locTuPian = '//a[text()="图片" and @target="_blank"]'  # 图片
# locTuPianSouSuo = '//input[@id="kw"]'  # 图片搜索框
# locTuPianBaiDuYiXia = '//input[@value="百度一下" and @class="s_newBtn"]'  # 图片百度一下
#
# # 【新知识】driver.window_handles：浏览器实例对象有一个属性叫windows_handles，作用就是获取窗口句柄列表
# beforeHandles = driver.window_handles
# # window = 窗口；handles = 句柄
# # print(f'没有点击图片之前的句柄个数：{len(beforeHandles)}，句柄信息：{beforeHandles}')
#
# driver.find_element(By.XPATH, locTuPian).click()  # 点击百度首页的【图片】
# time.sleep(2)  # 实际经验：当遇到有窗口切换，或者页面跳转的时候，为了脚本的稳定，建议，强制等待1~2秒
# # 点开新窗口以后，我们要做三步：
# # 第一步：拿到所有句柄，是Python的一个列表
# afterHandles = driver.window_handles
# # print(f'点击图片之后的句柄个数：{len(afterHandles)}，句柄信息：{afterHandles}')
# # 第二步：拿到句柄列表里的最新的句柄号，使用列表的下标-1来获取最后一个句柄
# newWindowHandle = afterHandles[-1]
# # 第三步，切换到新句柄（新窗口）：通过句柄号去切换
# # 使用driver浏览器实例对象下的switch_to方法下的window方法，传入句柄号，就能切换了
# # switch = 切换（不及物动词），所以要加介词to
# # switch_to下面其实有2个方法1个属性：
# # (1) 【切换窗口】 => window()  方法
# # (2) 切换frame网页框架 => frame()  方法
# # (3) 切换到弹出框 => alert  属性
# driver.switch_to.window(newWindowHandle)
# driver.find_element(By.XPATH, locTuPianSouSuo).send_keys('德云社')  # 在图片窗口中，输入内容
# time.sleep(3)
# driver.find_element(By.XPATH, locTuPianBaiDuYiXia).click()  # 在图片窗口中，点击【百度一下】
# time.sleep(3)
#
# # 关闭新窗口，回到老窗口的步骤
# # (1) close方法关闭当前激活的新窗口
# driver.close() # 关闭当前（当前句柄所在的）窗口
# time.sleep(2)
# # (2) switch_to.window()方法把句柄切换回老窗口
# driver.switch_to.window(afterHandles[0])
#
# # 定位元素
# driver.find_element(By.XPATH, '//input[@id="kw"]').send_keys('德云测')
# driver.find_element(By.XPATH, '//input[@id="su"]').click()
# # ================================

time.sleep(3)
driver.quit()
