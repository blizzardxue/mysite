#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
#python2.7x 
#send_simple_email_by_account.py  @2014-07-30 
#author: orangleliu 
 
'''''
使用python写邮件 simple
使用126 的邮箱服务
''' 
 
import smtplib 
from email.mime.text import MIMEText 
 
SMTPserver = 'smtp.sina.com' 
sender = 'blizzard_xue@sina.com' 
password = "9681125_lizhixue" 
 
message = 'I send a message by Python. 你好' 
msg = MIMEText(message) 
 
msg['Subject'] = 'Test Email by Python' 
msg['From'] = sender 
msg['To'] = '360959752@qq.com'
 
mailserver = smtplib.SMTP(SMTPserver, 25) 
mailserver.login(sender, password) 
mailserver.sendmail(sender, ['360959752@qq.com', 'li.zhixue@hotmail.com'], msg.as_string())
mailserver.quit() 
print('send email success')