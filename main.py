from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

from starlette.requests import Request

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {"data": "Welcome to the mailer - Gosu."}

@app.post("/debug", tags=["debug"])
def debug(request: Request) -> dict:
    print(request.form)
    print(request.json)
    print(request)
    dict = request.form
    for key in dict:
        print('form key '+dict[key])
    return {
        "data": {"Print Debug"}
    }

@app.post("/sendmail", tags=["sendmail"])
def send_mail(formData: dict) -> dict:
    print(formData)
    mail_content = 'Hello ' + str(formData['firstName']) + str(formData['mailBody']) + '. Please do not reply to this email as this mailbox is not monitored. Thanks, Teamli.'
    
    #The mail addresses and password
    
    sender_address = os.environ.get('SENDER_EMAIL_ID')
    sender_pass = os.environ.get('SENDER_PASSWORD')

    toaddr = os.environ.get('TO_EMAIL_ID')
    bccIds = os.environ.get('BCC_EMAIL_ID')
    bcc = [x.strip() for x in bccIds.lstrip(',').rstrip(',').split(',')]

    toaddrs = [toaddr] + bcc

    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['Subject'] = os.environ.get('MAIL_SUBJECT')
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)