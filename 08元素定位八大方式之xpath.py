# <input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">
# //input[@id="kw"]
# # //标签名[@属性名称="值"]
# //男[@长相="靠谱的" and @学历="本科" and @工资>她的]

# xPath是一套识别网页元素的语法
# 余老师写的：               //input[@id="kw"]  => 定位到元素的速度更快（性能更好）
# 语法解析：
# 一个下划线/代表绝对路径；两个下划线代表相对路径（一般都是用2个下划线）
# //标签名[@属性名称="值"]
# F12工具自动复制出来的xPath：//*[@id="kw"]

# 关于属性的原则： id -> name -> value -> 其他的
# 百度首页的搜索框
# <input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">
# //input[@id="kw"]

# 【百度一下】按钮
# <input type="submit" id="su" value="百度一下" class="bg s_btn">
# //input[@id="su"]

# // 新闻超链接
# <a href="http://news.baidu.com" target="_blank" class="mnav c-font-normal c-color-t">新闻</a>
# //a[text()="地图"]
# text()是一个xpath特殊函数，它可以让你直接找到网页显示文本的文字，替代 By.Link_text
# 扩展href属性：
# hyper reference = 超引用（超链接）

# // 关于百度
# <a class="text-color" href="//home.baidu.com" target="_blank">关于百度</a>
# 一般做法：
# //a[text()="关于百度"]
# 高级做法：
# //a[contains(text(), "关于")]  替代By.PARTIAL_LINK_TEXT
# contains(参数1, 参数2)函数：作用就是“包含”
# 参数1：text() 代表文本
# 参数2：值
# 语义：文本包含“关于”的
# 课堂作业：定位“使用百度前必读”
# //p[@class="lh"]//a[contains(text(), "必读")]

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
# 先写好所有需要抓取的元素的定位器
# loc = locator = 定位器
locSouSuoKuang = '//input[@id="kw"]'  # 百度首页搜索框
locBaiDuYiXia = '//input[@id="su"]'  # 百度一下按钮

# 定位搜索框元素
souSuoKuang = driver.find_element(By.XPATH, locSouSuoKuang)
# 在搜索框中输入内容
souSuoKuang.send_keys('德云测')
time.sleep(1)
# 定位百度一下按钮元素
baiDuYiXia = driver.find_element(By.XPATH, locBaiDuYiXia)
# 点击百度一下按钮
baiDuYiXia.click()
time.sleep(1)
# ================================

time.sleep(3)
driver.quit()

# 其他小用法
# //标签名[@属性]  # 定位具有某个属性的标签，标签没有属性值，或者有属性值但不填写

# 定位父元素：
# 元素标签/..
# 元素标签/parent::父元素的标签（轴定位的方式）

# 元素标签/标签  查找子级标签
# 元素标签//标签  查找后代标签（包含子级）

# Selenium和XPath的特殊用法
# 在查找到一个元素的基础上，再继续寻找这个元素里面的元素
# 已定位到的元素.find_element(By.XPATH, './里面的元素的表达式').click()
# 例如：elem.find_element(By.XPATH, './/input').click()
# 需要注意的是 ./ 是必须写的