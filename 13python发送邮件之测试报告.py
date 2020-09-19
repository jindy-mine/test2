"""
============================
Author:柠檬班-木森
Time:2020/4/9   20:20
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

"""
我qq邮箱的账号以及smtp服务的授权码
账号：musen_nmb@qq.com
授权码：algmmzptupjccbab

qq邮箱的smtp服务器地址：smtp.qq.com,端口：465
163邮箱的smtp服务器地址：smtp.163.com，端口：465 （25）

"""

# 第一步：连接smtp服务器，并登录
# 连接到smtp服务器
smtp = smtplib.SMTP_SSL(host="smtp.qq.com", port=465)
# 登录smtp服务器（邮箱账号和授权码进行登录，注意点：不是邮箱的密码）
smtp.login(user="musen_nmb@qq.com", password="algmmzptupjccbab")

# 第二步：构造一封多组件邮件
msg = MIMEMultipart()
msg["Subject"] = "上课邮件001"
msg["To"] = "lemonban@qq.com"
msg["From"] = "musen_nmb@qq.com"

# 构建邮件的文本内容
text = MIMEText("邮件中的文本内容", _charset="utf8")
msg.attach(text)

# 构造邮件的附件
with open(r"C:\project\py27_class\py27_api_test\reports\report.html","rb") as f:
    content = f.read()
report = MIMEApplication(content,_subtype=None)
report.add_header('content-disposition', 'attachment', filename='python.html')
msg.attach(report)

# 第三步：发送邮件
smtp.send_message(msg, from_addr="musen_nmb@qq.com", to_addrs=["3247119728@qq.com"])
