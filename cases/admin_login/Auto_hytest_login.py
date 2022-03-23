"""
@Project ：Auto_hytest 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/03/21
@File   :Auto_hytest_login.py
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from hytest import STEP,INFO,CHECK_POINT
from lib.common import *
import time

class UI_000x:
	
	ddt_cases = [
		{
			'name' : '管理员登录 不输入账号 - UI_0001',
			'para':[None,'88888888','请输入用户名']
		},
		{
			'name': '管理员登录 不输入密码 - UI_0002',
			'para': ['byhy', None,'请输入密码']
		},
		{
			'name': '管理员登录 输入错误账号 - UI_0003',
			'para': ['yuerwen', '88888888','登录失败 : 用户名或者密码错误']
		},
		{
			'name': '管理员登录 输入错误密码 - UI_0003',
			'para': ['byhy', '666666','登录失败 : 用户名或者密码错误']
		},
		{
			'name': '管理员登录 输入错误密码 - UI_0003',
			'para': [None, None, '请输入用户名']
		}
	]
	
	def teststeps(self):
		
		INFO('登录管理系统')
		# 调用全局共享 数据
		webDriver = GSTORE['webDriver']
		
		# 根据webdriver对象的get方法 打开指定的web地址
		web_file = r'http://127.0.0.1/mgr/sign.html'
		webDriver.get(web_file)
		
		# 取出参数
		username, password,tips = self.para
		if username is not None:
			webDriver.find_element(By.ID, 'username').send_keys(username)
		# 输入用户名和密码
		
		if password is not None:
			webDriver.find_element(By.ID, 'password').send_keys(password)
			
		# 点击按钮
		webDriver.find_element(By.CLASS_NAME, 'btn-primary').click()
		
		time.sleep(1)
		
		# 获取 弹窗提示信息
		notif = webDriver.switch_to.alert.text
		CHECK_POINT('检查提示信息',notif == tips)
		# 点击 OK 按钮
		webDriver.switch_to.alert.accept()
		
	def teardown(self):
		webDriver = GSTORE['webDriver']
		webDriver.find_element(By.CSS_SELECTOR,'#password').clear()
		webDriver.find_element(By.CSS_SELECTOR, '#username').clear()
		
	
		

		