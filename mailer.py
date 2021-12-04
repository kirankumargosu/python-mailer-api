import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


async def sendMail(formData: dict) -> dict:
    mail_content = 'Hello ' + str(formData['firstName']) + str(formData['mailBody']) + '. Please do not reply to this email as this mailbox is not monitored. Thanks, Teamli.'
    
    #The mail addresses and password
    sender_address = 'donotreplytmm@gmail.com'
    sender_pass = 'ximwoR-piknud-qoccu1'

    toaddr = 'themeadgatemagazine@gmail.com'
    bcc = ['kirankumar.gosu@gmail.com']

    toaddrs = [toaddr] + bcc

    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['Subject'] = 'Teamli | Message from Teamli'
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, toaddrs, text)
    session.quit()
    return {
        "data": {"Mail Sent"}
    }