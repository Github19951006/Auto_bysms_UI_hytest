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

force_tags = ['管理员操作','系统测试','UI测试']

class UI_0101:
	'''
	用例名称：
	管理员操作-UI_0101
	
	测试步骤：
	1. 使用正确的管理员账号、密码登录白月SMS系统
	2. 检查左侧菜单
	
	预期结果：
	2. 前三项菜单名称分别为：
		客户
		药品
		订单
	'''
	
	# 根据标签挑选
	tags = ['管理员操作','检查操作菜单','UI_0101']
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
	'''
	用例名称：
	管理员操作-UI_0102

	测试步骤：
	1. 使用正确的管理员账号、密码登录白月SMS系统
	2. 点击添加客户，输入客户名为 罗湖人民医院 的客户 电话、地址信息

	预期结果：
	1 登录成功
	2. 检查客户列表第一项结果中客户名、电话、地址信息都是正确的
	'''
	
	# 根据标签挑选
	tags = ['管理员操作', '添加客户信息', 'UI_0102']
	name = '添加客户信息 - UI-0102'
	
	def teststeps(self):
		
		STEP(1, '点击左侧菜单客户按钮_添加客户')
		area_click('客户')
		
		STEP(2, '添加单客户信息')
		add_customer_drugs_order(
			'添加单客户信息',['罗湖人民医院','0755-120','深圳市罗湖区友谊路人民医院']
		)
		
		STEP(3, '获取添加的客户信息')
		expected = [
			'客户名：',
			'罗湖人民医院',
			'联系电话：',
			'0755-120',
			'地址：',
			'深圳市罗湖区友谊路人民医院'
		]
		CHECK_POINT('检查获取的客户信息',
		            get_customer_drugs_order_info('客户信息') == expected
		            )
		

class UI_0103:
	'''
	用例名称：
	管理员操作-UI_0103

	测试步骤：
	1. 使用正确的管理员账号、密码登录白月SMS系统
	2. 点击添加客户，输入客户名为 罗湖人民医院 的客户
	然后再点击编辑，修改客户名为：罗湖人民中医院

	预期结果：
	1 登录成功
	2. 检查客户列表第一项结果中客户名、电话、地址信息都是正确的
	'''
	
	# 根据标签挑选
	tags = ['管理员操作', '修改客户信息', 'UI_0103']
	name = '修改客户信息 - UI-0103'
	
	def teststeps(self):
		webDriver = GSTORE['webDriver']
		STEP(1, '点击左侧菜单客户按钮_添加客户')
		area_click('客户')
		
		STEP(2, '添加单客户信息')
		add_customer_drugs_order(
			'添加单客户信息',['罗湖人民医院','0755-120','深圳市罗湖区友谊路人民医院']
		)
		
		STEP(3, '获取添加的客户信息')
		expected = [
			'客户名：',
			'罗湖人民医院',
			'联系电话：',
			'0755-120',
			'地址：',
			'深圳市罗湖区友谊路人民医院'
		]
		CHECK_POINT('检查获取的信息',
		            get_customer_drugs_order_info('客户信息') == expected
		            )
		
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
		
		CHECK_POINT('检查获取的客户信息',
		            get_customer_drugs_order_info('客户信息') == expected
		            )


class UI_0105:
	'''
	用例名称：
	管理员操作-UI_0105

	测试步骤：
	1.使用正确的管理员账号、密码登录白月SMS系统
	2.
	点击添加药品，输入正确格式的
	药品名、编号和
	描述
	
	预期结果：
	1 登录成功
	2. 检查药品列表第一项结果中 药品名、编号和 描述  都是正确的
	'''
	
	# 根据标签挑选
	tags = ['管理员操作', '添加药品信息', 'UI_0105']
	name = '添加药品信息 - UI-0105'
	def teststeps(self):
		# 引入浏览器驱动实例对象
		webDriver = GSTORE['webDriver']
		
		STEP(1, '点击左侧菜单药品按钮_添加药品')
		area_click('药品')
		
		STEP(2, '添加单药品信息')
		add_customer_drugs_order('添加单药品信息',['阿莫西林软膏','0001','中国好药膏'])
		
		STEP(3, '获取添加的药品信息')
		
		# 预期结果
		expected = ['药品：', '阿莫西林软膏', '编号：', '0001', '描述：', '中国好药膏']
		CHECK_POINT('检查获取的药品信息',
		            get_customer_drugs_order_info('药品信息') == expected
		            )


class UI_0107:
	'''
	用例名称：
	管理员操作-UI_0102

	测试步骤：
	1. 使用正确的管理员账号、密码登录白月SMS系统
	2. 在系统中添加3种药品，依次为
	'青霉素盒装1','YP-32342341','青霉素注射液，每支15ml，20支装'
	'青霉素盒装2','YP-32342342','青霉素注射液，每支15ml，30支装'
	'青霉素盒装3','YP-32342343','青霉素注射液，每支15ml，40支装'
	
	在系统中添加3个客户，依次为
	'南京中医院1','2551867851','江苏省-南京市-秦淮区-汉中路-501'
	'南京中医院2','2551867852','江苏省-南京市-秦淮区-汉中路-502'
	'南京中医院3','2551867853','江苏省-南京市-秦淮区-汉中路-503'
	
	进入订单管理界面，添加一个订单，
	客户选择 南京中医院2
	药品选择 青霉素盒装1
	数量填入 100盒

	预期结果：
	1 登录成功
	2. 添加订单成功
	'''
	# 根据标签挑选
	tags = ['管理员操作', '添加订单信息', 'UI_0107']
	name = '添加订单信息 - UI-0107'
	
	def teststeps(self):
		# 引入浏览器驱动实例对象
		webDriver = GSTORE['webDriver']
		
		STEP(1, '点击左侧菜单药品按钮_添加药品')
		area_click('药品')
		
		STEP(2, '添加多药品信息')
		# 添加药品信息
		add_customer_drugs_order('添加多药品信息', ['青霉素盒装','YP-3234234','青霉素注射液，每支'])
		
		STEP(3, '点击左侧菜单客户按钮_添加客户')
		area_click('客户')
		
		STEP(4, '添加多客户信息')
		add_customer_drugs_order('添加多客户信息',
		                         ['南方医科大学', '0755-120', '广东省-罗湖区-友谊路人民医院-50']
		                         )
		
		STEP(5, '点击左侧菜单订单按钮_添加订单')
		area_click('订单')
		
		STEP(6, '添加订单信息')
		add_customer_drugs_order('添加订单信息',
		                         ['Auto-yuerwen-test1','南方医科大学2', '青霉素盒装2', 100]
		                         )
		
		STEP(7, '获取添加的订单信息')
		# 预期结果
		expect = ['订单：',
		          'Auto-yuerwen-test1',
		          '客户：',
		          '南方医科大学2',
		          '药品：',
		          '青霉素盒装2 * 100'
		          ]
		CHECK_POINT('检查获取的药品信息',
		            get_customer_drugs_order_info('订单信息') == expect
		            )
		
		