import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service = Service(executable_path='D:\deyunce\pythondaima\selenium_40\drivers\chromedriver-win64\chromedriver.exe')
drive = webdriver.Chrome(service=service)
drive.implicitly_wait(10)  # 【新知识】隐式等待：设置等待元素定位的最大默认时间为10秒
# implicitily = 含蓄地；wait = 等待
# (1) 一个脚本，只需要写1次隐式等待就可以了，它是全局通用的（公共的等待）
# (2) 在Selenium3中，如果你不写隐式等待这句话，默认30秒；但是，从Selenium4(早期)开始，变成了”必填“，
# 如果不填，它默认等待0秒，会”无法定位到元素“；后面发现很多人不习惯，又改回3代的时候可以不写这句代码
# (3) 经验所谈，一般隐式等待的默认时间设置为10秒~15秒最常见
# (4) 即使有隐式等待，我们有时候依然需要利用强制等待的
# (5) 等待指的是定位一个元素，最多等待多少秒，假设设为10秒，即：等待定位到某个元素，最多等10秒，
# 大约每0.5秒，Selenium会去判断有没有找到对象，如果找到了，不继续等待剩余时间，
# 如果没找到，继续等待对象被找到，直到设定的10秒到了，报错：元素未找到
# (6) 隐式等待的缺点：它是根据HTML代码来识别是否找到元素的（这个元素的代码是不是已经在HTML网页里生成了），
# 有些元素控件你仅仅只是HTML源码里出现，其实界面上还没出现呢，这种情况下，隐式等待结束后，去操作对象，就会报错，比如：元素不可见
drive.maximize_window()  # 最大化浏览器窗口
drive.get('https://www.baidu.com')  # 进入网址


drive.quit()  # 退出并关闭浏览器（进程也会关闭）