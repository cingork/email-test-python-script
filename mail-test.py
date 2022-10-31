import smtplib

port = 465
smtp_server = "mailserver@mailserver.com"
sender_email= "sender@sender.com"
sender_password = "password"

message = "test message"
sent_to = ['cingork@gmail.com']
sent_subject = "Test email!"
sent_body = ("This is a test email message!\n\n"
             "I hope you recieve it!\n"
             "\n"
             "Regards,\n"
             "Görkem\n")

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sender_email, ", ".join(sent_to), sent_subject, sent_body)

with smtplib.SMTP_SSL(smtp_server,port) as server:
    try:
        server.ehlo()
        server.login(sender_email,sender_password)
        server.sendmail(sender_email,sent_to,email_text)
        server.close()
    except Exception as exception:
        print("Error: %s!\n\n" % exception)

