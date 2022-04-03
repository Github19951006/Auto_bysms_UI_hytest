"""
@Project ：Auto_hytest 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/03/22
@File   :common.py
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from hytest import *
import time


def open_browser():
	'''
	打开浏览器函数
	:return: 空
	'''
	
	# 创建一个webdriver 实例对象，指明使用Chrome浏览器驱动
	# 加上参数，禁止 chromedriver 日志写屏
	INFO('打开浏览器')
	options = webdriver.ChromeOptions()
	options.add_experimental_option(
		'excludeSwitches', ['enable-logging'])
	
	# 这里指定 options 参数
	webDriver = webdriver.Chrome(options=options)
	# 设置等等时间
	webDriver.implicitly_wait(5)
	
	# 存储 全局共享 数据
	GSTORE['webDriver'] = webDriver


def mgr_login():
	'''
	管理员登录
	:return:空
	'''
	INFO('登录管理系统')
	# 调用全局共享 数据
	webDriver = GSTORE['webDriver']
	
	# 根据webdriver对象的get方法 打开指定的web地址
	web_file = r'http://127.0.0.1/mgr/sign.html'
	webDriver.get(web_file)
	
	# 输入用户名和密码
	webDriver.find_element(By.ID, 'username').send_keys('byhy')
	webDriver.find_element(By.ID, 'password').send_keys('88888888')
	# 点击按钮
	webDriver.find_element(By.CLASS_NAME, 'btn-primary').click()
	
def delAll(webDriver):

    while True:
        # 修改全局等待时间，以免找不到元素，等待时间较长
        webDriver.implicitly_wait(1)
        # 找到所有删除按钮
        # 注意，一定要每次循环都 执行一遍，
        # 因为每次删除后，界面元素重新 产生了
        delButtons = webDriver.find_elements_by_css_selector(
            '.search-result-item-actionbar label:nth-last-child(1)')

        # 再改回原来的等待时间
        webDriver.implicitly_wait(5)

        # 没有删除按钮，说明已经全部删除了
        if not delButtons:
            break

        # 点击删除按钮
        delButtons[0].click()

        # 弹出对话框 点击确定
        webDriver.switch_to.alert.accept()

        # 等待1秒，等界面刷新
        time.sleep(1)

