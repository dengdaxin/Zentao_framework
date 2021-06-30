#!/usr/bin/env python
# encoding: utf-8


import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.read_config_utils import Config

class EmailUtils():
    def __init__(self,smtp_body,smtp_attch_path=None):
       self.smtp_server = Config.email_smtp_server
       self.smtp_sender = Config.email_smtp_sender
       self.smtp_password = Config.email_smtp_password
       self.smtp_receiver = Config.email_smtp_receiver
       self.smtp_cc = Config.email_smtp_cc
       self.smtp_subject = Config.email_smtp_subject
       self.smtp_body = smtp_body
       self.smtp_attch = smtp_attch_path

    def mail_message_body(self):
        message = MIMEMultipart()
        message['from'] = self.smtp_sender
        message['to'] = self.smtp_receiver
        message['Cc'] = self.smtp_cc
        message['subject'] = self.smtp_subject
        message.attach( MIMEText(self.smtp_body,'html','utf-8') )
        if self.smtp_attch:
            attach_file = MIMEText(open(self.smtp_attch, 'rb').read(), 'base64', 'utf-8')
            attach_file['Content-Type'] = 'application/octet-stream'
            attach_file.add_header('Content-Disposition', 'attachment', filename=('gbk', '', os.path.basename(self.smtp_attch)))
            message.attach(attach_file)
        return message

    def send_mail(self):
        smtp = smtplib.SMTP()
        smtp.connect(self.smtp_server)
        smtp.login(user=self.smtp_sender, password=self.smtp_password)
        smtp.sendmail(self.smtp_sender,self.smtp_receiver.split(",")+ self.smtp_cc.split(","), self.mail_message_body().as_string())

if __name__=='__main__':
    html_path = os.path.dirname(__file__) + '/../report/report2021.html'
    EmailUtils('<h3 align="center">自动测试报告</h3>',html_path).send_mail()