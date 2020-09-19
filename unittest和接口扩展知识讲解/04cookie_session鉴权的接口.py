"""
============================
Author:柠檬班-木森
Time:2020/4/14   21:10
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import requests
from requests import request

# 登录
login_url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
login_data = {
    "mobilephone": "13367899876",
    "pwd": "lemonban"
}
response = requests.post(url=login_url, data=login_data)

# print(response.text)
print(response.headers)
# print(response.json())
# # 获取http请求的状态码
# # print(response.status_code)
# # print(response.text)
# # print(response.json())
print("-*"*50)

# 调用充值的接口

recharge_url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
recharge_data = {
    "mobilephone": "13367899876",
    "amount": 2000
}
response2 = requests.post(url=recharge_url,data=recharge_data)
print(response2.text)