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
import logging
import hashlib
import os


logging.basicConfig(level=logging.INFO,filename='update.log',format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',datefmt='%a, %d %b %Y %H:%M:%S')

c = Connection("root@192.168.65.230",connect_kwargs={"password":"123"})
cn = Connection("root@192.168.65.170",connect_kwargs={"password":"123"})


def view():
	print("\t1.更新")
	print("\tq.退出")

def linux_md5(filename):

	jarhash = hashlib.md5()

	f = open(filename,'rb')
	b = f.read()
	jarhash.update(b)
	f.close()
	return jarhash.hexdigest()


#远程服务器执行命令
def update_dzyz():
	path_dzyz = '/data/install_dzyz/makeseal'
		
	linux_exec = input("请输入要执行的命令:")	
	with c.cd(path_dzyz):
		c.run(linux_exec)

#传输文件
def put_task(src_path,dst_path):
		
	cn.local("cd " + src_path)
	print(linux_md5(src_path + '/makeseal.jar'))
	
	
	c.put(src_path + "/makeseal.jar",dst_path + "/makeseal/")
	logging.info("传输成功")

	c.run("md5sum " + dst_path +  "/makeseal/makeseal.jar")


#调用函数,并进行判断执行的选项
while True:

	view()
	go = input("请输入你要选择的选项:")
	
	if go == '1':
		put_task(src_path = "/data/package",dst_path = "/data/install_dzyz")
		update_dzyz()
		print("成功")
	if go == 'q':
		sys.exit(0)


