import sendgrid
import os
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, Attachment, FileContent, FileName, FileType, Disposition
from python_http_client.exceptions import HTTPError
from info import info 

def email():
    sg = SendGridAPIClient(info.EMAIL_API_KEY)

    html_content = "<p>Daily hour report</p>"

    message = Mail(
        to_emails="antti.lecklin1@gmail.com",
        from_email=Email('antti.lecklin@gmail.com', "Proggis_3"),
        subject="Report on working hours",
        html_content=html_content
        )
    message.add_bcc("antti.lecklin@gmail.com")
    
    with open('dailyhour.txt', 'rb') as f:
        data = f.read()
        f.close()
    encoded_file = base64.b64encode(data).decode()

    attachedFile = Attachment(
    FileContent(encoded_file),
    FileName('dailyhour.txt'),
    FileType('text.txt'),
    Disposition('attachment')
    )
    message.attachment = attachedFile

    with open('dailyactivities.txt', 'rb') as f:
        data = f.read()
        f.close()
    encoded_file = base64.b64encode(data).decode()

    attachedFile2 = Attachment(
    FileContent(encoded_file),
    FileName('dailyactivities.txt'),
    FileType('text.txt'),
    Disposition('attachment')
    )
    message.attachment = attachedFile2

    try:
        response = sg.send(message)
        return f"email.status_code={response.status_code}"
        #expected 202 Accepted

    except HTTPError as e:
        return e.message

email()