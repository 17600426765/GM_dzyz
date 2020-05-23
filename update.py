#!/root/.pyenv/shims/python
# **********************************************************
# * Author        : kunyun
# * Email         : 
# * Create time   : 2020-05-23 09:25
# * Filename      : install.py
# * Description   : 
# **********************************************************


import sys
from fabric import Connection
#from fabric.api import run
import logging


logging.basicConfig(level=logging.INFO,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt='%a, %d %b %Y %H:%M:%S')

def view():
	print("\t1.更新")
	print("\tq.退出")

def update_dzyz():
	path_dzyz = '/data/'
	c = Connection("root@192.168.65.170",connect_kwargs={"password":"123"})
		
	
	with c.cd(path_dzyz):
		c.run('ls -l')
	

#调用函数,并进行判断执行的选项
while True:

	view()
	go = input("请输入你要选择的选项:")
	
	if go == '1':
		update_dzyz()
		print("成功")
	if go == 'q':
		sys.exit(0)


