import pandas as pd

with open('birthdays/birthday_mail.html') as f:
    html = f.readlines()
raw_body = '\n'.join(html)    
print(raw_body)


def get_all_bdays_email_body(bdays: pd.DataFrame, raw_body: str = raw_body):
    bdays_table_content = ""
    for _, row in bdays.iterrows():
        bdays_table_content += f"""\
        <tr>
            <td>{row["name"]}</td>
            <td>{row["birthday_date"]}</td>
            <td>{row["days_until_bday"]}</td>
        </tr>
        """

    email_html = raw_body.replace("$$TABLE_CONTENT$$", bdays_table_content)
    return email_html


def get_all_bdays_email_body_v2(bdays: pd.DataFrame, raw_body: str = raw_body):
    bdays_table_content = ""
    for _, row in bdays.iterrows():
        bdays_table_content += f"""\
        <tr style="height: 70px;">
            <td align="left">
                <p class="es-p10r es-p10l" style="font-size: 14px; font-family: manrope, arial, sans-serif;">{row["name"]}</p>
            </td>
            <td>
                <p class="es-p10r es-p10l" style="font-size: 14px; font-family: manrope, arial, sans-serif;">{row["birthday_date"]}</p>
            </td>
            <td class="es-p10r es-p10l" style="font-size: 14px; font-family: manrope, arial, sans-serif;">
                <p class="es-p10r es-p10l" style="font-size: 14px; font-family: manrope, arial, sans-serif;">{row["days_until_bday"]}</p>
            </td>
        </tr>
        """
            
    email_html = raw_body.replace("<!--TABLEDATA-->", bdays_table_content)
    return email_html

def sending_email(html: str):
    import smtplib
    import ssl
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    sender_email = "t7133657@gmail.com"
    receiver_email = ["t7133657@gmail.com"]
    password = "jwmo yrmh kafo wjns "
    cc = ["marijn2huis@gmail.com", "pimduif@gmail.com", "t7133657@gmail.com"]


    message = MIMEMultipart("alternative")
    message["Subject"] = "Birthday Message"
    message["From"] = sender_email
    message["To"] = ",".join(receiver_email)
    message["Cc"] = ",".join(cc)

    # Turn these into plain/html MIMEText objects
    body = MIMEText(html, "html")

    message.attach(body)

    # creates SMTP session, start TLS for securty and authenticate
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    # sending the mail and terminate the session
    server.sendmail(sender_email, receiver_email + cc, message.as_string())
    server.quit()
