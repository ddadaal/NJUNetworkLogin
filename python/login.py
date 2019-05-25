import urllib.request
import urllib.parse
import json
import settings
from datetime import datetime

username=settings.username
password=settings.password

if (username=="用户名") or (password=="密码"):
    print("先编辑settings.py文件设置用户名和密码。")
    exit()

url="http://p.nju.edu.cn/portal_io/login"
value={"username":username, "password":password}

data=urllib.parse.urlencode(value).encode("ascii")
req=urllib.request.Request(url,data)
with urllib.request.urlopen(req) as response:
    encoding=response.headers.get_content_charset()
    page=response.read().decode(encoding)
    
result=json.loads(page)
result_code=int(result['reply_code'])

if result_code in (1,6):
    if result_code==1:
        print("登录成功！\n")
    else:
        print("已经登录！\n")
    name=result['userinfo']['fullname']
    balance=result['userinfo']['balance']
    time=datetime.fromtimestamp(int(result['userinfo']['acctstarttime']))
    print(name)
    print("本次登录时间：{0}".format(time))
    print("余额：{0}".format(balance))
    
if result_code==3:
    print("密码错误！编辑settings.py文件设置用户名和密码。")
