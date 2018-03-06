# encoding:utf-8

import smtplib, os, csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def sendreport():
    sender = 'ceshi@xin-group.com'
    receivers = 'luochengmei@xin-group.com'
    data = csv.reader(open(r"%s\..\data\email.csv" % os.getcwd(), 'rb'))
    memberlist = []
    for c in data:
        memberlist.append(c[0])
    memberlist.append(receivers)

    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("AutoTest", 'utf-8')
    message['To'] = Header("", 'utf-8')
    subject = 'erp自动化测试报告'
    message['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText('详情见附件...', 'plain', 'utf-8'))

    # 构造附件
    result_dir = r"%s\..\reports" % os.getcwd()
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not
    os.path.isdir(result_dir+"\\"+fn) else 0)
    print('The lasted report: '+lists[-1])
    file_new = os.path.join(result_dir,lists[-1])
    print(file_new)

    att1 = MIMEText(open(file_new, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="report.html"'
    message.attach(att1)

    try:
        smtpObj = smtplib.SMTP('imap.xin-group.com')
        smtpObj.login(sender, "123456")
        smtpObj.sendmail(sender, memberlist, message.as_string())
        print("Email sent successfully!")
    except smtplib.SMTPException:
        print("Error, Email sent unsuccessfully!")


# import smtplib, csv, os
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.application import MIMEApplication
# from email.header import Header
#

# def sendreport():
#     data = csv.reader(open(r"%s\..\data\1.csv" % os.getcwd(), 'rb'))
#     member = []
#     for c in data:
#         member.append(c[0])
#     From = "ceshi@xin-group.com"
#     To = "zhangyinhao@xin-group.com"
#     member.append(To)
#
#     result_dir = r"%s\..\reports" % os.getcwd()
#     lists=os.listdir(result_dir)
#     lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not
#     os.path.isdir(result_dir+"\\"+fn) else 0)
#     print (u'最新测试生成的报告： '+lists[-1])
#     # 找到最新生成的文件
#     file_new = os.path.join(result_dir,lists[-1])
#     print file_new
#
#     server = smtplib.SMTP("imap.xin-group.com")
#     server.login("ceshi@xin-group.com","123456")  # 仅smtp服务器需要验证时
#
#     # 构造MIMEMultipart对象做为根容器
#     main_msg = email.MIMEMultipart.MIMEMultipart()
#
#     # 构造MIMEText对象做为邮件显示内容并附加到根容器
#     text_msg = email.MIMEText.MIMEText("详情见附件...")
#     main_msg.attach(text_msg)
#
#     # 构造MIMEBase对象做为文件附件内容并附加到根容器
#     contype = 'application/octet-stream'
#     maintype, subtype = contype.split('/', 1)
#
#     # 读入文件内容并格式化
#     data = open(file_new, 'rb')
#     file_msg = email.MIMEBase.MIMEBase(maintype, subtype)
#     file_msg.set_payload(data.read())
#     data.close()
#     email.Encoders.encode_base64(file_msg)
#
#     # 设置附件头
#     basename = os.path.basename(file_new)
#     file_msg.add_header('Content-Disposition',
#      'attachment', filename = basename)
#     main_msg.attach(file_msg)
#
#     # 设置根容器属性
#     main_msg['From'] = From
#     main_msg['To'] = To
#     main_msg['Subject'] = "erp系统自动化测试报告"
#     main_msg['Date'] = email.Utils.formatdate()
#
#     # 得到格式化后的完整文本
#     fullText = main_msg.as_string()
#
#     # 用smtp发送邮件
#     try:
#         server.sendmail(From, member, fullText)
#     finally:
#         server.quit()
#     print '邮件已发出!'
