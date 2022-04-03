"""
@Project ：Auto_hytest 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/03/25
@File   :add_user.py
"""
from lib.common import *
from selenium.webdriver.support.ui import Select
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
		# 获取左侧菜单，点击订单按钮
		webDriver.find_elements(
			By.CSS_SELECTOR, '.sidebar-menu span'
		)[2].click()
		
		# 添加客户
		webDriver.find_element(
			By.CSS_SELECTOR, '.add-one-area .btn'
		).click()
		
	# 缓存1s
	time.sleep(1)
	
def add_customer_drugs_order(info,info_list):
	'''
	add_customer_drugs_order :添加客户、药品、订单信息方法
	:return:
	'''
	
	webDriver = GSTORE['webDriver']
	if info == '添加单客户信息':
		# 添加客户信息
		col_elemet = webDriver.find_element(By.CLASS_NAME, 'add-one-area')
		col_elemet.find_element(By.CLASS_NAME, 'btn-md').click()
		form_controls = col_elemet.find_elements(By.CLASS_NAME, 'form-control')
		form_controls[0].send_keys(info_list[0])
		form_controls[1].send_keys(info_list[1])
		form_controls[2].send_keys(info_list[2])
		
		# 点击创建按钮
		col_elemet.find_element(By.CLASS_NAME, 'btn-xs').click()
		
	if info == '添加多客户信息':
		# 添加客户信息
		col_elemet = webDriver.find_element(By.CLASS_NAME, 'add-one-area')
		col_elemet.find_element(By.CLASS_NAME, 'btn-md').click()
		form_controls = col_elemet.find_elements(By.CLASS_NAME, 'form-control')
		
		number = 0
		while number < 3:
			form_controls[0].send_keys(f'{info_list[0]}{number + 1}')
			form_controls[1].send_keys(f'{info_list[1]}{number + 1}')
			form_controls[2].send_keys(f'{info_list[2]}{number + 1}')
			number = number + 1
			
			# 点击创建按钮
			col_elemet.find_element(By.CLASS_NAME, 'btn-xs').click()
		
	if info == '添加单药品信息':
		# 获取添加药品的详细详细
		elements = webDriver.find_elements(By.CSS_SELECTOR, '.add-one-area .col-sm-8 .form-control:nth-of-type(1)')
		# - 药品名称
		elements[0].send_keys(info_list[0])
		# - 编号
		elements[1].send_keys(info_list[1])
		# - 描述
		elements[2].send_keys(info_list[2])
		# - 点击确定
		webDriver.find_element(By.CSS_SELECTOR, '.add-one-area .btn-xs').click()
		
	if info == '添加多药品信息':
		# 添加药品信息
		div_elemets = webDriver.find_elements(
			By.CSS_SELECTOR, '.add-one-area .col-sm-8 div [class="form-control"]'
		)
		i = 0
		while i < 3:
			div_elemets[0].send_keys(f'{info_list[0]}{i + 1}')
			div_elemets[1].send_keys(f'{info_list[1]}{i + 1}')
			div_elemets[2].send_keys(f'{info_list[2]}，{(i + 2) * 10}支装')
			i = i + 1
			# 点击创建按钮
			webDriver.find_element(
				By.CSS_SELECTOR, '.add-one-area .col-sm-12 [type="button"]'
			).click()
		
	if info == '添加订单信息':
		# 设置等等时间
		webDriver.implicitly_wait(5)
		# 输入订单名称
		webDriver.find_element(
			By.CSS_SELECTOR, '.add-one-area  .form-control'
		).send_keys(info_list[0])
		
		# 获取两个select 对象
		select_elements = webDriver.find_elements(By.CSS_SELECTOR, '.add-one-area select')
		# 选择客户
		Select(select_elements[0]).select_by_visible_text(info_list[1])
		# 选择药品
		Select(select_elements[1]).select_by_visible_text(info_list[2])
		
		webDriver.find_element(
			By.CSS_SELECTOR, 'input[type = "number"]'
		).send_keys(info_list[3])
		
		# 点击创建按钮
		webDriver.find_element(
			By.CSS_SELECTOR, '.add-one-area .btn-xs'
		).click()
		
	# 缓存1s
	time.sleep(1)
	
def get_customer_drugs_order_info(info):
	'''
	get_customer_drugs_order_info:获取用户添加后的客户、药品、订单信息的方法
	返回一个信息列表
	:return: result_element_itemrs_list
	'''
	webDriver = GSTORE['webDriver']
	result_element = webDriver.find_element(By.CLASS_NAME, 'search-result-item')
	result_element_itemrs = result_element.find_elements(
		By.CLASS_NAME, 'search-result-item-field')
	
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
	
	if info == '订单信息':
		# 获取药品订单信息，存储到 search_result_item_list 列表中
		spans = webDriver.find_elements(
			By.CSS_SELECTOR, '.content-wrapper .container-fluid '
			                 '.search-result-item span'
		)
		p_element = webDriver.find_element(
			By.CSS_SELECTOR, '.content-wrapper .container-fluid '
			                 '.search-result-item p'
		)
		# 获取订单的信息
		search_result_item_list = [e.text for e in spans[:2]]
		for e in spans[4:7]:
			search_result_item_list.append(e.text)
		# 获取p标签的 青霉素信息和个数
		search_result_item_list.append(p_element.text)
		INFO(search_result_item_list)
		return search_result_item_list