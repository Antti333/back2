def email(request):
    import os
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail, Email
    from python_http_client.exceptions import HTTPError

    sg = SendGridAPIClient(os.environ['EMAIL_API_KEY'])

    html_content = "<p>Hello World!</p>"

    message = Mail(
        to_emails="[Destination]@email.com",
        from_email=Email('[YOUR]@gmail.com', "Your name"),
        subject="Hello world",
        html_content=html_content
        )
    message.add_bcc("[YOUR]@gmail.com")

    try:
        response = sg.send(message)
        return f"email.status_code={response.status_code}"
        #expected 202 Accepted

    except HTTPError as e:
        return e.message