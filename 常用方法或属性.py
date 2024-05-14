# 浏览器实例对象(driver)
# driver.maximize_window()  最大化浏览器
# driver.get('网址全名')  进入网址
# driver.quit()  退出浏览器，关闭浏览器实例（后台的进程里就没有了）
# driver.find_element('By.方式', '值')  找单个元素，返回网页元素的实例对象（没找到，则报错）
# 找元素的八大方式：
# By.ID  通过ID的方式
# By.NAME  通过NAME的方式
# By.LINK_TEXT  通过网页链接元素的显示文字的方式
# By.PARTIAL_LINK_TEXT  通过网页链接元素的“部分”显示文字的方式
# By.TAG_NAME  通过标签名称的方式
# By.CLASS_NAME  通过标签中的class类属性的方式
# By.XPATH  通过XPATH语法的方式
# By.CSS_SELECTOR  通过CSS语法的方式
# driver.window_handles  【属性】获取当前浏览器所有打开的标签页窗口的句柄，存入一个句柄列表中
# driver.current_window_handle  【属性】获取当前所激活的窗口的句柄号
#     current 当前的；window 窗口；handle 句柄号
# driver.switch_to.window(句柄编号)  传入你要切换的窗口句柄编号进行切换
#     switch to 切换
# alert_object = driver.switch_to.alert  【属性】切入到浏览器弹出框的窗口，并返回该窗口的实例对象
#     基于窗口对象，一共提供有4种操作：
#     alert_object.text  【属性】获得窗口对象的提示词
#     alert_object.send_keys()  在弹出框中的输入框，进行内容的输入
#     alert_object.accept()  点击弹出框中的【确定】按钮
#     alert_object.dismiss()  点击弹出框中的【取消】按钮进行驳回
# driver.close()  关闭当前所激活的句柄的所在窗口
#     close 关闭
# driver.switch_to.frame(定位方式)  切入指定框架
#     切框架有3种方法
#     (1) 通过框架的下标编号进行切换（余老师最不推荐的）
#     dr.switch_to.frame(0)  好像有bug，有时候切不进去
#     (2) 通过框架id切换（前提：该框架元素需要有id属性）
#     dr.switch_to.frame('login_frame')
#     (3) 通过定位到的框架元素进行切换（最万能，最好的一种）
#         传入的是一个元素，不是一个元素定位器
# driver.switch_to.default_content()  直接切回主框架（无论你现在在多么深的框架内）
# driver.switch_to.parent_frame()  切入到上一层框架
# ActionChains(浏览器实例对象driver).move_to_element(元素对象)  鼠标移动到指定的元素
# ActionChains(浏览器实例对象driver).行为1().行为n().perform()  链条中有多个行为
#     生效链条操作，一定要最后点出perform方法
# ActionChains(浏览器实例对象driver).pause(秒数).perform  停顿
# ActionChains(浏览器实例对象driver) .key_down(Keys.键).perform() 按下某个键，不松开
# ActionChains(浏览器实例对象driver).key_up(Keys.键).perform()  松开某个键
# ActionChains(浏览器实例对象driver).send_keys_to_element(元素, 输入内容).perform()
#
# Select(select标签的属性).select_by_index(下标)  支持单选和多选
# Select(select标签的属性).select_by_value(option选项标签的value属性)  支持单选和多选
# Select(select标签的属性).select_by_visible_text(选项的文本显示值)  支持单选和多选
#
# Select(select_elem).deselect_by_index(下标)  根据下标反选
# Select(select_elem).deselect_by_value(选项的value属性的值)  根据value属性的值反选
# Select(select_elem).deselect_by_visible_text(文本显示值)  根据文本显示值反选
# Select(select_elem).deselect_all()  反选所有
#
# Select(select标签的属性).first_selected_option.text
#     first_selected_option属性返回的是一个元素，元素再点出text属性
# Select(select标签的属性).options  【属性】获取所有下拉框中的选项元素，存入一个列表中
#
# driver.execute_script(js)  执行js脚本，常常用于临时修改时间控件，使它可以输入
#
# WebDriverWait(浏览器实例对象driver, 最长等待时间).util(EC.visibility_of_element_located(定位器元组), 没找到元素的时候的提示语[可选])
#     定位器元组：(By.XPATH, '//input[@id="kw"]')
#     (1) 智能等待，需要导包：WebDriverWait, expected_conditions 然后别名成EC
#     (2) 我们只会用到util
#     (3) 常用的预期条件：
#         visibility_of_element_located  判断元素在网页上可见了
#         frame_to_be_available_and_switch_to_it  判断框架存在，如果存在则自动切入
#     (4) WebDriverWait智能等待的返回值值：
#         如果找到元素，返回WebElement，即：该元素对象
#         如果无法找到元素，返回TimeOutException，超时的异常错误
#
# 网页元素实例对象(web_element)
# web_element.send_keys('输入的内容')  输入框元素进行键盘发送
# web_element.click()  点击网页元素（按钮类、链接类）
# web_element.clear()  输入框元素清空当前所输入的内容
# web_element.text  链接类元素对象的【属性】：文本显示值
