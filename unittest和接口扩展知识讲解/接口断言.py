"""
============================
Author:柠檬班-木森
Time:2020/4/14   20:04
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

#  邮箱已注册
expected = {
    "email": [
        "此邮箱已注册"
    ]
}

res = {
    "email": [
        "此邮箱已注册"
    ]
}

# assert expected == res

# 注册成功的情况
expected1 = {
    "username": "musenww01"
}

# 实际结果
res1 = {
    "id": 1659,
    "username": "musenww01",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNjU5LCJ1c2VybmFtZSI6Im11c2Vud3cwMSIsImV4cCI6MTU4Njk1MjMzNSwiZW1haWwiOiJtdXNlbjA4ODJAcXEuY29tIn0.ACuGW5kukoQjlv1K6UE-4er3l7vL57wOvdpgiTrxGi4"
}


# assert expected1 in res1


def assert_dict(expected, res):
    """
    自定义 用来对连个字典进行成员运算断言的方法
    :param expected: 预期结果
    :param res: 实际结果
    :return:
    """
    for key in expected:
        # 判断键是否存在,键对应的值也相等
        if key in res.keys() and expected[key] == res[key]:
            # 这个键对应的值是否一致,断言通过
            pass
        else:
            raise AssertionError("断言不通过")


#
# assert_dict(expected1, res1)
# assert_dict(expected, res)

li = [1, 2, 3,555]
li2 = [12, 3, 4, 521, 1, 2, 3]
# assert li in li2

def list_in(list1,list2):
    """
    :param list1: 预期
    :param list2: 实际
    :return:
    """
    for li in list1:
        if li in list2:
            pass
        else:
            raise AssertionError("{} not in{}，断言不通过".format(list1,list2))


list_in(li,li2)