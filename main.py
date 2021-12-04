from fastapi import FastAPI
import mailer as m

app = FastAPI()


@app.get("/")
def read_root():
    return {"200": "Welcome To Mailer"}

@app.post("/sendmail", tags=["sendmail"])
def send_mail(formData: dict) -> dict:
    m.sendMail(formData=formData)
    return {
        "data": {"Mail Sent"}
    }

