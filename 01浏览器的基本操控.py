# 浏览器的基本操控
# (1) 启动浏览器
# (2) 把浏览器最大化
# (3) 打开网址
# (4) 关闭浏览器

# (1) 启动浏览器
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Step1: 实例化Service类，放入executable_path参数，给到一个实例对象，一般取名为service
# executable_path 驱动的文件路径
# 绝对路径写法：D:\DeyuncePythonStudy\WebAutomation25\drivers\chromedriver.exe
# 相对路径写法：./drivers/chromedriver.exe
service = Service(executable_path='./drivers/chromedriver.exe')
# Step2: 导入webdriver，点出Chrome类，放入service参数，把刚才第1步中获得的实例化对象service传进去，
# 最后得到了一个新的实例化，一般我们喜欢叫driver，接下来大多数操作，都是这个driver变量（实例化对象）进行点出来的
driver = webdriver.Chrome(service=service)
# dirver = 驾驶员、驱动
# 其实，webdriver.Chrome(service=service)就是启动浏览器

# (2) 最大化浏览器
time.sleep(1)
# sleep = 睡眠
driver.maximize_window()
# maximize window 最大化窗口

# (3) 打开某个网址
time.sleep(1)
driver.get('https://www.baidu.com')

# (4) 关闭浏览器
# 使用quit方法
# quit = 退出、离开
time.sleep(3)
driver.quit()