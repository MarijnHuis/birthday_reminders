import smtplib

# message to be sent
message = """\
Subject: Hi There
This message is send from Python."""

# creates SMTP session, start TLS for securty and authenticate
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("t7133657@gmail.com", "-")
# sending the mail and terminate the session
server.sendmail("t7133657@gmail.com", "pimduif@gmail.com", message)
server.quit()