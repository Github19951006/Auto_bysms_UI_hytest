"""
@Project ：Auto_hytest 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/03/26
@File   :auto_hytest_windows.py
"""
from lib.add_user import *
import time

class UI_0106:
	'''
	用例名称：
	管理员操作-UI_0106

	测试步骤：
	1. 使用正确的管理员账号、密码登录白月SMS系统
	2. 点击页脚处 链接 白月黑羽教学使用，点击访问官网
	然后 在新打开的 白月黑羽教学网页，获取 页眉导航菜单中所有教程类目
	（ 可以调用webdriver对象的maximize_window()方法最大化窗口，以便显示所有菜单 ）
	3. 随后再回到 白月SMS系统网页，点击退出登录

	预期结果：
	1 登录成功
	2. 导航菜单名 依次为
	Python基础
	Python进阶
	Web开发
	自动化和性能测试
	练习作业
	常见问题
	好文分享
	3.  验证回到登录界面（可以根据webdriver对象的current_url属性判断是否进入登录页面）

	'''
	tags = ['UI_0106', '系统测试','窗口切换']
	name = '窗口切换 - UI-0106'
	
	# 初始化方法
	def setup(self):
		open_browser()
		mgr_login()
	
	def teststeps(self):
		webDriver = GSTORE['webDriver']
		
		STEP(1, '点击页脚处链接’白月黑羽教学使用，点击访问官网‘')
		# 创建mainWindow变量保存当前窗口的句柄
		mainWindow = webDriver.current_window_handle
		
		# 点击跳转到学习官网
		webDriver.find_element(
			By.CSS_SELECTOR,'.main-footer .pull-right a[href]'
		).click()
		
		STEP(2, '切换到白月黑羽官网窗口')
		# 切换到打开的新窗口网页
		for handle in webDriver.window_handles:
			# 先切换到该窗口
			webDriver.switch_to.window(handle)
			# 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
			if '白月黑羽' in webDriver.title:
				# 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
				break
				
		# 缓存1s
		time.sleep(1)
		
		STEP(3, '获取导航栏菜单的信息')
		# 获取导航栏菜单的信息
		spans = webDriver.find_elements(
			By.CSS_SELECTOR, '#navbar-content .d-md-inline-flex span')
		span_list = [span.text for span in spans]
		INFO(span_list)
		
		# 预期信息
		expect = ['Python基础', 'Python进阶', '图形界面程序', 'Web开发', '自动化测试', '性能测试', '其它']
		CHECK_POINT('检查导航栏菜单的信息',span_list == expect )

		# 通过前面保存的老窗口的句柄，自己切换到老窗口
		webDriver.switch_to.window(mainWindow)
	