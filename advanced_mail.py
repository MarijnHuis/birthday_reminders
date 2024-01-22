import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "t7133657@gmail.com"
receiver_email = ["marijn2huis@gmail.com"]
password = "-"
cc = ['marijn2huis@gmail.com', 'pimduif@gmail.com', 't7133657@gmail.com']

message = MIMEMultipart("alternative")
message["Subject"] = "Birthday Message"
message["From"] = sender_email
message["To"] = ','.join(receiver_email)
message['Cc'] = ','.join(cc)

# Create the plain-text and HTML version of your message
text = """\
Hi Big T,
How are you?
It's Rory's birthday in 1 week.
"""

html = """\
<html>
  <body>
    <h1>Hi Big T</h1>
    <p>How are you?<br>
        It's Rory's birthday in 1 week. If you need a present, click
       <a href="https://www.bol.com/nl/nl/p/mankini-borat-string/9200000103544012/">here</a>.
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

message.attach(part1)
message.attach(part2)

# creates SMTP session, start TLS for securty and authenticate
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
# sending the mail and terminate the session
server.sendmail(sender_email, receiver_email+cc, message.as_string())
server.quit()