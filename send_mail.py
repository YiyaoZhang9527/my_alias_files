import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv ,find_dotenv
from pathlib import Path
import os
from log_color import log,LogLevel
load_dotenv(find_dotenv(Path.cwd().joinpath('qqpassword.env')),verbose=True)

default_key= os.getenv("QQ_PASSWORD0") #邮箱授权码
print(default_key)

def send_email(receiverMail="408903228@qq.com" #接受者邮件地址
             ,subject = "自动邮件测试" #邮件主题
             ,content = "hello dear" #邮件内容
             ,authCode = default_key
             ,senderMail = '408903228@qq.com' #发送者地址邮箱
            ):
    msg = MIMEText(content,"plain","utf-8")
    msg['Subject'] = subject
    msg['From'] = senderMail
    msg['To'] = receiverMail
    try:
        server = smtplib.SMTP_SSL('smtp.qq.com', smtplib.SMTP_SSL_PORT)
        log('成功连接到邮件服务器',level=LogLevel.PASS)
        server.login(senderMail, authCode)
        log('成功登录邮箱',level=LogLevel.PASS)
        server.sendmail(senderMail, receiverMail, msg.as_string())
        log('邮件发送成功',level=LogLevel.PASS)
    except smtplib.SMTPException as e:
        log(f'邮件发送异常 : {e}', level=LogLevel.DEBUG)
    finally:
        server.quit()
        
        
if __name__ == '__main__':
    log("请输入对方邮箱地址:",level=LogLevel.INFO)
    mail_address = input()
    log("请输入邮件主题:",level=LogLevel.INFO)
    mail_subject = input()
    log("请输入邮件正文:",level=LogLevel.INFO)
    mail_body = input()
    send_email(receiverMail=mail_address,subject=mail_subject,content=mail_body)