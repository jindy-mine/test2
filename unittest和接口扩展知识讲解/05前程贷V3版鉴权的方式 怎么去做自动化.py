"""
============================
Author:柠檬班-木森
Time:2020/4/14   21:37
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import time
from common.handle_sign import HandleSign

token = "q2weretryfgyihfdsadsfdgfhjhgfdasfgdhgjhdsfgfgjhgf"

# # 获取当前的时间戳
# s = int(time.time())
# # token前50位和时间戳拼接
# msg = token[:50]+str(s)
#
# sign = HandleSign.to_encrypt(msg=msg)
# print(sign)

data ={"name":1111,"pwd":2222}

sign_data = HandleSign.generate_sign(token)

print(sign_data)

data.update(sign_data)
print(data)