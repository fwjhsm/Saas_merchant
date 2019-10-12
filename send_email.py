import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from Saas_merchant.TestRunner import filename


def send_mail(file_new):
    f = open (os.getcwd()+"\\report_html\\"+file_new, 'rb')
    filename = f.read ()
    print(filename)
    f.close ()
    smtp = smtplib.SMTP ()
    smtp.connect ('smtp.163.com')      #服务器
    sender = 'fengjie_w1@163.com'      #发件人邮箱
    receiver = '2808369777@qq.com'    #收件人邮箱
    username = 'fengjie_w1@163.com'   #账号
    password = 'fwj961205' #网易授权码，不是密码
    smtp.login (username, password)

    subject = '附件为最新测试报告，望查收'
    msg = MIMEText (filename, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告",'utf-8')
    msg['From'] = 'Tim<fengjie_w1@163.com>'
    msg['To'] = '2808369777@qq.com'
    smtp.sendmail (sender, receiver, msg.as_string ())
    smtp.quit ()

    print ('email has send out!')

send_mail(filename)