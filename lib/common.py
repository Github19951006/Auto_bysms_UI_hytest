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