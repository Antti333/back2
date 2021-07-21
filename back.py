def email():
    import os
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail, Email
    from python_http_client.exceptions import HTTPError

    sg = SendGridAPIClient(os.environ['EMAIL_API_KEY'])

    html_content = "<p>Hello World!</p>"

    message = Mail(
        to_emails="antti.lecklin1@gmail.com",
        from_email=Email('antti.lecklin@gmail.com', "Proggis_3"),
        subject="Hello world",
        html_content=html_content
        )
    message.add_bcc("antti.lecklin@gmail.com")

    try:
        response = sg.send(message)
        return f"email.status_code={response.status_code}"
        #expected 202 Accepted

    except HTTPError as e:
        return e.message

email()