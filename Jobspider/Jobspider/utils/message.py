# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def sendMessage_warning():
    server = smtplib.SMTP('localhost', 25)
    server.login('761471746@qq.com', 'fengtuiyu1108')
    msg = MIMEText('爬虫Master被封警告！请求解封！', 'plain', 'utf-8')
    msg['From'] = '761471746@qq.com <761471746@qq.com>'
    msg['Subject'] = Header(u'爬虫被封禁警告！', 'utf8').encode()
    msg['To'] = u'warm<878836747@qq.com>'
    server.sendmail('761471746@qq.com', ['878836747@qq.com'], msg.as_string())