from fastapi import FastAPI, BackgroundTasks, UploadFile, File, Form
from starlette.responses import JSONResponse
from starlette.requests import Request
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from app.configs.Config import MailConfig
from typing import List


conf = ConnectionConfig(
    MAIL_USERNAME=MailConfig.MAIL_USERNAME,
    MAIL_PASSWORD=MailConfig.MAIL_PASSWORD,
    MAIL_FROM=MailConfig.MAIL_FROM,
    MAIL_PORT=MailConfig.MAIL_PORT,
    MAIL_SERVER=MailConfig.MAIL_SERVER,
    MAIL_TLS=MailConfig.MAIL_TLS,
    MAIL_SSL=MailConfig.MAIL_SSL,
    USE_CREDENTIALS=MailConfig.USE_CREDENTIALS,
    VALIDATE_CERTS=MailConfig.VALIDATE_CERTS
)

async def send_email(subject: str, recipient: List, message: str):
    message = MessageSchema(
        subject=subject,
        recipients=recipient,
        body=message,
    )
    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})     

