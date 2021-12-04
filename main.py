from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
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
    return {"200": "Welcome To Mailer"}

@app.post("/sendmail", tags=["sendmail"])
def send_mail(formData: dict) -> dict:
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)