#!/usr/bin/python
#coding=utf-8

import smtplib
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

host_server = 'smtp.163.com' # 新浪邮箱smtp服务器
sender_sina = 'neilchallenge@163.com' # 发件人邮箱
pwd = 'wangyismtp1'

# receiver = '1277762246@qq.com' # 收件人地址
receiver = '1228395301@qq.com'

mail_title = '邮件标题' # 邮件标题
mail_content = '这是python自动发送的邮件，邮件内容是我随便写的' # 邮件内容

msg = MIMEMultipart() # 主体
msg['Subject'] = Header(mail_title, 'utf-8')
msg['From'] = sender_sina
msg['To'] = Header(receiver, 'utf-8')
msg.attach(MIMEText(mail_content, 'plain', 'utf-8'))

smtp = SMTP_SSL(host_server) # 连接服务器
smtp.login(sender_sina, pwd)
smtp.sendmail(sender_sina, receiver, msg.as_string())
smtp.quit()
