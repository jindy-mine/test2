"""
============================
Author:柠檬班-木森
Time:2020/4/14   20:33
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import unittest
from requests import request
from unittest.mock import Mock

"""


gen_sign("musen")
使用用户名，和时间进行加密得到一个加密的签名数据

"""
gen_sign = Mock(return_value="yJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJf")



class TestLogin(unittest.TestCase):

    def test_login(self):
        data = {
            "user": "musne",
            "pwd": "ldjfss",
            "sign": gen_sign("musen")
        }
        url = "http://127.0.0.1:8000/login"

        reponse = request(url=url,json=data,method="post")
