import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 【知识补充】
# selenium去除“Chrome正受到自动软件测试的控制”提示
# (1) 添加一个Chrome的option配置，得到配置实例
# (2) 在webdriver实例化Chrome浏览器的时候，添加一个参数chrome_options，把配置实例赋值给它
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
service = Service(executable_path='./drivers/chromedriver.exe')
dr = webdriver.Chrome(service=service, chrome_options=option)
dr.implicitly_wait(10)
dr.maximize_window()
dr.get('http://deyunce:911917@hospital.deyunce.com/sel/toLogin')
time.sleep(2)

locYongHuMing = 'input#loginname'  # 用户名
locMiMA = 'input#pwd'  # 密码
locDengLu = 'button[lay-filter="login"]'  # 登录
locHouTaiShouYe = '//cite[text()="后台首页"]'  # 后台首页
locGuanLiYuan = '//span[text()="管理员"]'  # 管理员
locTuiChu = '//cite[text()="退出"]'  # 退出

# 登录
yongHuMing = dr.find_element(By.CSS_SELECTOR, locYongHuMing)  # 定位用户名对象
yongHuMing.send_keys('dycadmin')  # 输入用户名
dr.find_element(By.CSS_SELECTOR, locMiMA).send_keys('123456')  # 输入密码
dr.find_element(By.CSS_SELECTOR, locDengLu).click()  # 点击【登录】
time.sleep(2)  # 目的是为了让脚本稳定

# 验证是否登录成功
# 【重点】每当切换页面后，我们需要去找一个能够证明你已经在这个页面上的元素，用is_displayed方法来检查是否显示，显示就代表页面切换成功
# is_displayed方法的作用就是去查看元素是否在页面上显示，显示则返回True，不显示则返回False
houTaiShouYeShiFouXianShi = dr.find_element(By.XPATH, locHouTaiShouYe).is_displayed()
print(f'后台首页是否显示：{houTaiShouYeShiFouXianShi}')

# 退出登录
guanLiYuan = dr.find_element(By.XPATH, locGuanLiYuan)
ActionChains(dr).move_to_element(guanLiYuan).perform()
time.sleep(0.5)  # 目的是为了让脚本稳定
dr.find_element(By.XPATH, locTuiChu).click()
time.sleep(2) # 目的是为了让脚本稳定

# 验证是否退出成功
yongHuMingShiFouXianShi = yongHuMing.is_displayed()  # 用户名对象不需要再重新定位，复用即可
print(f'用户名是否显示：{yongHuMingShiFouXianShi}')

time.sleep(3)
dr.quit()
