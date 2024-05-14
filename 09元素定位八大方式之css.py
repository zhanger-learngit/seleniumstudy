# 真正在工作中，只会用xpath和css两种选一个
# css其实就是样式，通过样式选择器的方式也能够定位网页元素的
# 样式选择器

# 你觉得xpath好还是css好，外面市面上，基本55开的，有些人喜欢xpath，有些人喜欢css
# 常见的面试题：你觉得CSS和XPATH哪种定位方式好，有什么区别？
# 区别就是定位表达式不一样，然后css定位速度比xpath略快；
# 大多数情况下，表达式更简短；
# 但是一些很复杂的定位(回穿)，css不太方便，需要用xpath的轴定位
# 定位网页链接显示文字，css不支持
# 最佳解决方案，如果喜欢用CSS的，其实也是和XPATH的混用
# 定位元素的速度：
# 谷歌浏览器：css方式的定位速度比xpath快（0.5~2秒）
# 火狐浏览器，两者几乎一致，只差0.几秒
# IE浏览器：反而xpath还比css快
# Edge浏览器：内核是谷歌的，所以CSS快

# 定位百度搜索框：
# id = "kw"
# CSS表达式： #kw
# XPATH表达式：//*[@id="kw"]

# CSS常用语法
# 井号#代表id属性
#kw   =>  寻找id属性的值是kw的元素，css里值不需要加一对引号（发现有7个）

# input#kw   =>  寻找input标签下的id属性是kw的，就唯一定位

# 通过属性去定位
# css定位写法
# input[name="wd"]
# 多条件：input[id="kw"][name="wd"]

# xpath定位写法
# //input[@name="wd"]

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

service = Service(executable_path='D:\DeyuncePythonStudy\selenium学习\drivers\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get('https://www.baidu.com')
time.sleep(2)

# =========== 新知识区 ============
driver.find_element(By.CSS_SELECTOR, '#kw').send_keys('CSS是个啥')

# ================================

time.sleep(3)
driver.quit()

# 其他小用法
# 标签
# 标签[属性]
# [属性]

# 查找子级：父元素 > 子元素
# 查找后代：父元素 后代元素

# 查找后面紧挨着的第一个兄弟：哥哥标签 + 弟弟标签
# 查找后面的所有的兄弟：哥哥标签 ~ 弟弟标签

# 找祖先元素
# 祖先标签:has(子标签)
# 其实就是含有某个子标签的祖先标签