"""
@Project ：Auto_hytest 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/03/21
@File   :Auto_hytest.py
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from hytest import STEP,INFO,CHECK_POINT
from lib.common import *
import time

class UI_0101:
	name = '检查操作菜单 - UI_0101'
	
	def teststeps(self):
		
		STEP(1, '打开浏览器，登录网站')
		open_browser()
		mgr_login()
		
		STEP(2,'获取左侧菜单信息')
		webDriver = GSTORE['wd']
		
		sidebar_menu = webDriver.find_element(By.CLASS_NAME, 'sidebar-menu')
		span_lists = sidebar_menu.find_elements(By.TAG_NAME, 'span')
		menuText = [span.text for span in span_lists]
		INFO(menuText[:3])
		
		STEP(3,'检查菜单栏信息')
		CHECK_POINT('左侧菜单检查',menuText[:3] == ['客户', '药品', '订单'])
		
		webDriver.quit()
		
class UI_0102:
	name = '添加客户信息 - UI_0102'
	
	def teststeps(self):
		
		STEP(1, '打开浏览器，登录网站')
		open_browser()
		mgr_login()
		
		STEP(2,'点击左侧菜单客户按钮')
		webDriver = GSTORE['wd']
		
		webDriver.find_element(
			By.CLASS_NAME, 'add-one-area'
		).click()
		
		# 缓存1s
		time.sleep(1)
		
		STEP(3,'添加客户信息')
		col_elemet = webDriver.find_element(By.CLASS_NAME, 'add-one-area')
		col_elemet.find_element(By.CLASS_NAME, 'btn-md').click()
		form_controls = col_elemet.find_elements(By.CLASS_NAME, 'form-control')
		form_controls[0].send_keys('罗湖人民医院')
		form_controls[1].send_keys('0755-120')
		form_controls[2].send_keys('深圳市罗湖区友谊路人民医院')
		# 点击创建按钮
		col_elemet.find_element(By.CLASS_NAME, 'btn-xs').click()
		# 缓存1s
		time.sleep(1)
		
		STEP(4,'获取添加的客户信息')
		result_element = webDriver.find_element(By.CLASS_NAME, 'search-result-item')
		result_element_itemrs = result_element.find_elements(By.CLASS_NAME, 'search-result-item-field')
		
		# 存储客户信息相关的列表
		result_element_itemrs_list = []
		for e in result_element_itemrs:
			for e in e.find_elements(By.TAG_NAME, 'span'):
				result_element_itemrs_list.append(e.text)
		INFO(result_element_itemrs_list)
		expected = [
			'客户名：',
			'罗湖人民医院',
			'联系电话：',
			'0755-120',
			'地址：',
			'深圳市罗湖区友谊路人民医院'
		]
		CHECK_POINT('客户信息检查',result_element_itemrs_list == expected)
		
		webDriver.quit()
		