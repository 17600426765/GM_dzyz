#!/root/.pyenv/shims/python
# **********************************************************
# * Author        : kunyun
# * Email         : 
# * Create time   : 2020-05-26 08:53
# * Filename      : login_md5.py
# * Description   : 
# **********************************************************


import hashlib

user_list = []

def get_md5(data):
    obj = hashlib.md5("12:;idrsicxwersdfsaersdfsdfresdy54436jgfdsjdxff123ad".encode('utf-8'))
    obj.update(data.encode('utf-8'))
    result = obj.hexdigest()
    return result

def register():
    print("++++++++用户注册++++++++")
    while True:
        user = input("请输入用户名:")
        if user == "N":
            return
        pwd = input("请输入密码:")
        temp = {'username':user,'password':pwd}
        user_list.append(temp)
        print(user_list)

def login():
        print("++++++++用户登录++++++++")
        user = input("请输入用户名:")
        pwd = input("请输入密码:")

        for item in user_list:
            if item['username'] == user and get_md5(item['password']) == get_md5(pwd):
                return True

register()
result = login()

if result:
    print("登录成功")
else:
    print("登录失败")
