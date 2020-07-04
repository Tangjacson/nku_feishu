# -*- coding:utf8 -*-

# 导入selenium2中的webdriver库

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import datetime
import time

# 实例化出一个Firefox浏览器
options = webdriver.ChromeOptions()
options.add_argument('--disable-extensions')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(chrome_options=options, executable_path="/tmp/chromedriver")

# 设置浏览器窗口的位置和大小
driver.set_window_position(20, 40)
driver.set_window_size(1100, 700)

# enter through feishu
driver.get("https://www.feishu.cn/suite/passport/oauth/?app_id=4e11974c58ae389b&desc=%7B%22default%22%3A%22%E5%8D%97%E5%BC%80%E5%BE%AE%E5%BA%94%E7%94%A8%22%2C%22en-US%22%3A%22%E5%8D%97%E5%BC%80%E5%BE%AE%E5%BA%94%E7%94%A8%22%2C%22ja-JP%22%3A%22%E5%8D%97%E5%BC%80%E5%BE%AE%E5%BA%94%E7%94%A8%22%2C%22zh-CN%22%3A%22%E5%8D%97%E5%BC%80%E5%BE%AE%E5%BA%94%E7%94%A8%22%7D&redirect_uri=https%3A%2F%2Fopen.feishu.cn%2Fopen-apis%2Fauthen%2Fv1%2Fauthen_pc%3Fapp_id%3Dcli_9ef30c5ece29100d%26redirect_uri%3Dhttps%253A%252F%252Ffeishu.nankai.edu.cn%252FFeishu%252FIndex%252Fcheckin%253Furl%253D%25252Fhome%25252Findex%25252Fredirectapplication%25253Fappid%25253D229%26response_type%3Dcode%26state%3D&response_type=token&sign=cf1aa75f331d9263a04dd048374f708102b2ddd5ce9612b1a3795a81ad14920e&state=7469821f-9733-42a8-881e-10573210f9a9")
# switch to account login
a = driver.find_element_by_css_selector('[class="switch-login-mode-btn-icon account-icon"]')
driver.execute_script('arguments[0].click()',a)
time.sleep(1)
# enter via sso
a1 = driver.find_element_by_xpath('//div[@class="pp-base-button base-button base-button-plainborder base-button-round sso-login-sso-button"]')
driver.execute_script('arguments[0].click()', a1)
time.sleep(1)
# pass throught nankai account test
driver.find_element_by_css_selector('[data-test="login-set-idp-input"]').send_keys('nankai')
driver.find_element_by_css_selector('[data-test="login-set-idp-input"]').send_keys(Keys.ENTER)
# 通过使用选择器选择到表单元素进行模拟输入和点击按钮提交
time.sleep(2)
driver.find_element_by_css_selector('[name="urpid"]').clear()
driver.find_element_by_css_selector('[id="inputUrpid"]').send_keys('id')
driver.find_element_by_css_selector('[id="inputPassword"]').clear()
driver.find_element_by_css_selector('[id="inputPassword"]').send_keys('passwd')  # password
driver.find_element_by_css_selector('[id="inputPassword"]').send_keys(Keys.ENTER)  # password
# driver.find_element_by_css_selector('[type="submit"]').click()
time.sleep(2)
now = datetime.datetime.now()
if (now.hour >= 13):
    time.sleep(5)
    dig_alert = driver.switch_to.alert
    # 打印警告对话框内容
    print(dig_alert.text)
    # alert对话框属于警告对话框，我们这里只能接受弹窗
    dig_alert.accept()

# 选择体温
time.sleep(5)
ele = driver.find_element_by_css_selector('[id="q1"]')
s = Select(ele)
s.select_by_value("36.4")

html = driver.page_source
print(html)
# 确认提交
driver.find_element_by_css_selector('[onclick="fnSaveBtnSubmit()"]').click()
#确认并退出窗口
tanchuang = driver.switch_to.alert
tanchuang.accept()
time.sleep(2)
driver.quit()
