import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path='./drivers/chromedriver.exe')
dr = webdriver.Chrome(service=service)
dr.maximize_window()
dr.get('https://mail.qq.com/')
time.sleep(3)

# =================== 新知识 =======================
# iframe就是网页的框架标签
# frame = 框架
# 如果你要操控的元素在某个框架内，需要先切入到框架，才可以找到该元素
# 切框架有3种方法
# (1) 通过框架的下标编号进行切换（余老师最不推荐的）
# dr.switch_to.frame(0)  # 好像有bug，有时候切不进去
# (2) 通过框架id切换（前提：该框架元素需要有id属性）
# dr.switch_to.frame('login_frame')
# (3) 通过定位到的框架元素进行切换（最万能，最好的一种）
# iframe = dr.find_element(By.XPATH, '//iframe[@name="login_frame"]')
# dr.switch_to.frame(iframe)

# # ============== 第一种：通过框架的下标进行切入 =================
# dr.switch_to.frame(1)  # 外层框架
# dr.switch_to.frame(0)  # 内层

# ============== 第二种：通过框架的id进行切入 =================
dr.switch_to.frame(1)  # 外层框架（无id）
dr.switch_to.frame('ptlogin_iframe')  # 内层框架（有id）

# ============== 第三种：通过frame框架元素切入 =================
# # 定位外框架
# locWaiKuangJia = 'iframe[class="QQMailSdkTool_login_loginBox_qq_iframe"]'
# # 切入外框架
# dr.switch_to.frame(dr.find_element(By.CSS_SELECTOR, locWaiKuangJia))  # 传入的是框架元素而不是元素定位器
# 定位内框架
# locNeiKuangJia = 'iframe#ptlogin_iframe'
# neiKuangJia = dr.find_element(By.CSS_SELECTOR, locNeiKuangJia)
# # 切入内框架
# dr.switch_to.frame(neiKuangJia)  # 传入的是框架元素而不是元素定位器

# 然后点击密码登录，最后输入QQ号
dr.find_element(By.CSS_SELECTOR, 'a#switcher_plogin').click()  # 点击密码登录
time.sleep(1)
dr.find_element(By.CSS_SELECTOR, 'input#u').send_keys('12345678')  # 输入QQ号
time.sleep(2)

# 切入框架以后，在完成了所有该框架内需要进行的操作后，千万不要忘了，切回主框架
dr.switch_to.default_content() # 切回网页主框架
# default = 默认；content = 内容；网页的默认内容不就是主框架的内容
dr.find_element(By.XPATH, '//a[text()="基本版"]').click()

# dr.switch_to.parent_frame()  # 扩展知识：切回到上一层框架

time.sleep(1)

dr.quit()
