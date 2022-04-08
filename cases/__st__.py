"""
@Project ：Auto_hytest 
@Author : 文跃锐（yuerwen）
@University:东莞理工学院
@Time   : 2022/03/23
@File   :__st__.py
"""
from lib.common import *

def suite_setup():
	INFO('suite_setup')
	open_browser()
	mgr_login()

# 初始清除
def suite_teardown():
	INFO('suite_teardown')
	webDriver = GSTORE['webDriver']
	webDriver.quit()
