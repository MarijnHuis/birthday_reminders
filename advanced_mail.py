import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "t7133657@gmail.com"
receiver_email = ["t7133657@gmail.com"]
password = "jwmo yrmh kafo wjns"
# cc = ['marijn2huis@gmail.com', 'pimduif@gmail.com', 't7133657@gmail.com']

message = MIMEMultipart("alternative")
message["Subject"] = "Birthday Message"
message["From"] = sender_email
message["To"] = ','.join(receiver_email)
# message['Cc'] = ','.join(cc)

placeholder = 'ronald'
# Create the plain-text and HTML version of your message
text = """\
Hi Big T,
How are you?
It's Rory's birthday in 1 week.
"""

html = f"""\
<html>
  <body>
    <h1>Verjaardag reminder</h1>
    <p> Het is {placeholder} zijn verjaardag over {placeholder} dagen.
    </p>
    <div class="table">
      <h1>Komende verjaardagen</h1>
        <table class="table-data">
            <tr>
                <th>Naam</th>
                <th>Datum</th>
                <th>Dagen</th>
            </tr>
            <tr>
                <td>Tijn</td>
                <td>10 Augustus</td>
                <td>100</td>
            </tr>
            <tr>
                <td>Kwint</td>
                <td>11 Augustus</td>
                <td>20</td>
            </tr>
        </table>
    </div>
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
server.sendmail(sender_email, receiver_email, message.as_string())
server.quit()