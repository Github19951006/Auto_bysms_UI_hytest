"""
@Project ：Auto_hytest 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/03/25
@File   :add_user.py
"""
from lib.common import *
import time

def area_click(info):
	'''
	area_click:点击左侧菜单客户按钮
	:return:
	'''
	webDriver = GSTORE['webDriver']
	
	# 判断左侧操作菜单栏按钮信息
	if info == '客户':
		# 点击左侧菜单客户按钮
		webDriver.find_element(
			By.CSS_SELECTOR,
			'.sidebar-menu li:nth-last-of-type(4) span'
		).click()
		
		webDriver.find_element(
			By.CLASS_NAME, 'add-one-area'
		).click()
	
	if info == '药品':
		# 点击左侧菜单客户按钮
		webDriver.find_element(
			By.CSS_SELECTOR,
			'.sidebar-menu li:nth-last-of-type(3) span'
		).click()
		
		# - 点击添加药品按钮
		webDriver.find_element(
			By.CSS_SELECTOR, '.add-one-area button'
		).click()
	
	if info == '订单':
		# 点击左侧菜单客户按钮
		webDriver.find_element(
			By.CSS_SELECTOR,
			'.sidebar-menu li:nth-last-of-type(2) span'
		).click()
		
		webDriver.find_element(
			By.CLASS_NAME, 'add-one-area'
		).click()
		
	# 缓存1s
	time.sleep(1)
	
def add_customer_drugs_order(info):
	'''
	add_customer :添加客户信息方法
	:return:
	'''
	
	webDriver = GSTORE['webDriver']
	if info == '添加客户信息':
		# 添加客户信息
		col_elemet = webDriver.find_element(By.CLASS_NAME, 'add-one-area')
		col_elemet.find_element(By.CLASS_NAME, 'btn-md').click()
		form_controls = col_elemet.find_elements(By.CLASS_NAME, 'form-control')
		form_controls[0].send_keys('罗湖人民医院')
		form_controls[1].send_keys('0755-120')
		form_controls[2].send_keys('深圳市罗湖区友谊路人民医院')
		# 点击创建按钮
		col_elemet.find_element(By.CLASS_NAME, 'btn-xs').click()
		
	if info == '添加药品信息':
		# 获取添加药品的详细详细
		elements = webDriver.find_elements(By.CSS_SELECTOR, '.add-one-area .col-sm-8 .form-control:nth-of-type(1)')
		# - 药品名称
		elements[0].send_keys('阿莫西林软膏')
		# - 编号
		elements[1].send_keys('0001')
		# - 描述
		elements[2].send_keys('中国好药膏')
		# - 点击确定
		webDriver.find_element(By.CSS_SELECTOR, '.add-one-area .btn-xs').click()
		
	# 缓存1s
	time.sleep(1)
	
def get_customer_drugs_orderinfo(info):
	'''
	get_customer_inf:获取用户添加后信息的方法
	返回一个信息列表
	:return: result_element_itemrs_list
	'''
	webDriver = GSTORE['webDriver']
	result_element = webDriver.find_element(By.CLASS_NAME, 'search-result-item')
	result_element_itemrs = result_element.find_elements(By.CLASS_NAME, 'search-result-item-field')
	if info == '客户信息':
		# 存储客户信息相关的列表
		result_element_itemrs_list = []
		for e in result_element_itemrs:
			for e in e.find_elements(By.TAG_NAME, 'span'):
				result_element_itemrs_list.append(e.text)
		INFO(result_element_itemrs_list)
		return result_element_itemrs_list
	
	if info == '药品信息':
		# 判断用例是否通过
		# 获取前面的6个text文本信息，存储到list中
		if_elements = webDriver.find_elements(
			By.CSS_SELECTOR, '.container-fluid .search-result-item span')[:6]
		texts = [e.text for e in if_elements]
		INFO(texts)
		return texts