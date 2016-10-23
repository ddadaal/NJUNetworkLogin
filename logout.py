import urllib.request
import urllib.parse
import json
from datetime import datetime

url="http://p.nju.edu.cn/portal_io/logout"

req=urllib.request.Request(url)
urllib.request.urlopen(req)

print("已登出")