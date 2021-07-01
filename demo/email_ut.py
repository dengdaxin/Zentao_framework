import smtplib  #发送邮件 smtp简单邮件传输协议
from email.mime.text import MIMEText    #写正文
from email.mime.multipart import MIMEMultipart   #传附件
from email.header import Header   #邮件收件人 主题等2
from common.read_config_utils import Config

def seamil(fname,file1):
    #sender='1964518019@qq.com' #收件人邮箱
    revicer=[Config.email_smtp_receiver,'874077486@qq.com']

    #设置邮件头部（收件人，发件人，邮件主题）
    message=MIMEMultipart()
    message['From']=Header('dengdaxin','utf-8')  #发件人
    message['to']=Header('uiuiui','utf-8')  #收件人
    subject = Config.email_smtp_subject
    message['Subject']=Header(subject,'utf-8')

    #设置邮件正文 三个参数意义：正文内容、plain-纯文本、编码方式
    message.attach(MIMEText('UI自动化测试报告','plain','utf-8'))
    #设置邮件的附件
    part1 = MIMEText(open(fname,'rb').read(),'base64','utf-8')
    part1['Content-Type']='applicat ion/octet-stream'

    #设置收到附件后，显示的名字
    part1['Content-Disposition']='attachment;filename='+file1
    message.attach(part1)
    #发邮件
    smtpobj=smtplib.SMTP(Config.email_smtp_server) #第三方邮箱服务器地址

    #登录邮箱的账号和密码
    smtpobj.login(Config.email_smtp_sender,Config.email_smtp_password)

    smtpobj.sendmail(Config.email_smtp_receiver,revicer,message.as_string())