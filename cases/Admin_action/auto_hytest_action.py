"""
@Project ：Auto_hytest 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/03/21
@File   :Auto_hytest_action.py
"""
from lib.common import *
from lib.add_user import *
import time

force_tags = ['管理员操作','冒烟测试','UI测试']

class UI_0101:
	# 根据标签挑选
	tags = ['管理员操作','系统测试']
	
	name = '检查操作菜单 - UI-0101'
	
	def teststeps(self):
		
		STEP(1,'获取左侧菜单信息')
		webDriver = GSTORE['webDriver']
		
		sidebar_menu = webDriver.find_element(By.CLASS_NAME, 'sidebar-menu')
		span_lists = sidebar_menu.find_elements(By.TAG_NAME, 'span')
		menuText = [span.text for span in span_lists]
		INFO(menuText[:3])
		
		STEP(2,'检查菜单栏信息')
		CHECK_POINT('左侧菜单检查',menuText[:3] == ['客户', '药品', '订单'])
		
		
		
class UI_0102:
	name = '添加客户信息 - UI-0102'
	
	def teststeps(self):
		
		STEP(1, '点击左侧菜单客户按钮')
		area_click()
		
		STEP(2, '添加客户信息')
		add_customer()
		
		STEP(3, '获取添加的客户信息')
		expected = [
			'客户名：',
			'罗湖人民医院',
			'联系电话：',
			'0755-120',
			'地址：',
			'深圳市罗湖区友谊路人民医院'
		]
		CHECK_POINT('检查获取的信息', get_customer_info() == expected)
		

class UI_0103:
	name = '添加客户信息 - UI-0103'
	
	def teststeps(self):
		webDriver = GSTORE['webDriver']
		STEP(1, '点击左侧菜单客户按钮')
		area_click()
		
		STEP(2, '添加客户信息')
		add_customer()
		
		STEP(3, '获取添加的客户信息')
		expected = [
			'客户名：',
			'罗湖人民医院',
			'联系电话：',
			'0755-120',
			'地址：',
			'深圳市罗湖区友谊路人民医院'
		]
		CHECK_POINT('检查获取的信息',get_customer_info() == expected)
		
		STEP(4,'修改客户信息')
		# 获取添加的客户信息
		item = webDriver.find_element(By.CLASS_NAME, 'search-result-item')
		# 点击编辑按钮pr
		item.find_element(By.CLASS_NAME, 'btn-xs').click()
		
		# 修改客户的信息
		item.find_element(By.CLASS_NAME, 'form-control').clear()
		item.find_element(By.CLASS_NAME, 'form-control').send_keys('罗湖人民中医院')
		item.find_element(By.CLASS_NAME, 'btn-xs').click()
		
		result_element_itemrs = item.find_elements(By.CLASS_NAME, 'search-result-item-field')
		
		print('-----修改客户的信息-----')
		result_element_itemrs_list = []
		STEP(5, '获取修改的客户信息')
		
		# 校验：检查输入的客户信息
		expected = [
			'客户名：',
			'罗湖人民中医院',
			'联系电话：',
			'0755-120',
			'地址：',
			'深圳市罗湖区友谊路人民医院'
		]
		
		CHECK_POINT('检查获取的信息', get_customer_info() == expected)