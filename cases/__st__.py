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


class MySignalHandler:
	TEST_RET_COL_NO = 6  # 测试结果在用例excel文件中的列数

	def __init__(self):
		self.caseNum2Row = {}  # 用例编号->行数 表
		self.getCaseNum2RowInExcel()

		import win32com.client
		self.excel = win32com.client.Dispatch("Excel.Application")
		self.excel.Visible = True
		workbook = self.excel.Workbooks.Open(r"D:\bysms\bysms_cases.xlsx")
		self.sheet = workbook.Sheets(1)

	def getCaseNum2RowInExcel(self):
		"""
		得到Excel 中用例 编号对应的行数，方便填写测试结果
		"""
		import xlrd
		book = xlrd.open_workbook(r"D:\bysms\bysms_cases.xlsx")
		sheet = book.sheet_by_index(0)
		caseNumbers = sheet.col_values(colx=1)
		print(caseNumbers)

		for row, cn in enumerate(caseNumbers):
			if '-' in cn:
				self.caseNum2Row[cn] = row + 1

		print(self.caseNum2Row)

	def case_result(self, case):
		"""
		case_result 是 每个用例执行结束 ，会调用的函数

		@param case: 用例类 实例
		"""

		# 找到对应的测试用例在excel中的行数
		caseNo = case.name.split(' - ')[-1].strip()
		cell = self.sheet.Cells(self.caseNum2Row[caseNo], self.TEST_RET_COL_NO)
		# 翻动滚动条，保证当前测试结果单元格可见
		self.excel.ActiveWindow.ScrollRow = self.caseNum2Row[caseNo] - 2

		if case.execRet == 'pass':
			cell.Value = 'pass'
			cell.Font.Color = 0xBF00  # 设置为绿色
		else:
			cell.Font.Color = 0xFF  # 设置为红色
			if case.execRet == 'fail':
				cell.Value = 'fail'
			elif case.execRet == 'abort':
				cell.Value = 'abort'

	def test_end(self, runner):
		"""
		test_end 是 整个测试执行完 ，会调用的函数

		@param runner :  hytest runner 对象
			   runner.case_list:  列表，里面包含了所有用例类实例
		"""
		for case in runner.case_list:
			print(f'{case.name} --- {case.execRet}')


# 注册这个类的实例 为一个 hytest 信号处理对象
from hytest import signal

signal.register(MySignalHandler())
	