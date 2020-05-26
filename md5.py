#!/root/.pyenv/shims/python
# **********************************************************
# * Author        : kunyun
# * Email         : 
# * Create time   : 2020-05-25 08:53
# * Filename      : md5.py
# * Description   : 
# **********************************************************

# -*- encodig: utf-8 -*-

import hashlib
import os
import datetime

def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename,'rb')
    b = f.read()
    myhash.update(b)
    f.close()
    return myhash.hexdigest()

filepath = input("请输入文件路径:")

starttime = datetime.datetime.now()
print(GetFileMd5(filepath))
endtime = datetime.datetime.now()
print("运行时间:{}".format((endtime-starttime).seconds))
