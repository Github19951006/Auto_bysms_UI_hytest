"""
@Project ：Auto_hytest 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/03/25
@File   :add_user.py
"""
from lib.common import *
import time

def area_click():
	'''
	area_click:点击左侧菜单客户按钮
	:return:
	'''
	webDriver = GSTORE['webDriver']
	
	# 点击左侧菜单客户按钮
	webDriver.find_element(
		By.CLASS_NAME, 'add-one-area'
	).click()
	
	# 缓存1s
	time.sleep(1)
	
def add_customer():
	'''
	add_customer :添加客户信息方法
	:return:
	'''
	
	webDriver = GSTORE['webDriver']
	
	# 添加客户信息
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
	
def get_customer_info():
	'''
	get_customer_inf:获取用户添加后信息的方法
	返回一个信息列表
	:return: result_element_itemrs_list
	'''
	webDriver = GSTORE['webDriver']
	result_element = webDriver.find_element(By.CLASS_NAME, 'search-result-item')
	result_element_itemrs = result_element.find_elements(By.CLASS_NAME, 'search-result-item-field')
	
	# 存储客户信息相关的列表
	result_element_itemrs_list = []
	for e in result_element_itemrs:
		for e in e.find_elements(By.TAG_NAME, 'span'):
			result_element_itemrs_list.append(e.text)
	INFO(result_element_itemrs_list)
	return result_element_itemrs_list
	