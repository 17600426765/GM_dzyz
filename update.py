#!/root/.pyenv/shims/python
# **********************************************************
# * Author        : kunyun
# * Email         : 
# * Create time   : 2020-05-23 09:25
# * Filename      : install.py
# * Description   : 
# **********************************************************

import sys

def view():
	print("\t1.更新")
	print("\tq.退出")
	


#调用函数,并进行判断执行的选项
while True:

	view()
	go = input("请输入你要选择的选项:")
	
	if go == '1':
		print("成功")
	if go == 'q':
		sys.exit(0)


