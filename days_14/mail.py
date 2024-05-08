from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

def main():
    sender = 'coc1D100success@163.com'
    receivers = [
        'zhangzehui607@163.com',
        'zzh2589234570@gmail.com'
    ]
    message = MIMEText('code for test','plain','utf-8')
    message['From'] = Header('张泽辉','utf-8')
    message['To'] = Header('佛耶戈','utf-8')
    message['Subject'] = Header('code for test in example','utf-8')
    smtper = SMTP('smtp.163.com')
    smtper.login(sender,'QSJAVPFDRFXJMMLL')
    smtper.sendmail(sender,receivers,message.as_string())
    print('mail has send!')

if __name__ == '__main__':
    main()