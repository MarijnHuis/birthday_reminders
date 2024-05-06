import os
import pandas as pd

def get_all_bdays_email_body(bdays, days: int, bday_boy: list):
    with open("birthdays/templates/template_0day.html") as f:
        html = f.readlines()
    raw_body = "\n".join(html)

    dict_days =  {0 : 'vandaag',
                    1 : 'over 1 dag',
                    7 : 'over 7 dagen'}
    
    if len(bday_boy) == 1:
        email_message = f"Boys, {bday_boy[0]} is {dict_days[days]} jarig."
    
    elif len(bday_boy) > 1:
        bday_string = ' & '.join(filter(None, [', '.join(bday_boy[:-1])] + bday_boy[-1:]))
        email_message = f"Boys, {bday_string} zijn {dict_days[days]} jarig."

    email_html = raw_body.replace("<!--TABLEDATA-->", email_message)
    return email_html

def get_all_bdays_email_body_month(bdays: pd.DataFrame):
    
    with open("birthdays/birthday_mail.html") as f:
        html = f.readlines()
    raw_body = "\n".join(html)

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


def sending_email(html: str, email_list: list):
    import smtplib
    import ssl
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    sender_email = "t7133657@gmail.com"
    receiver_email = email_list
    password = "ubij cyhq iqob ntss"
    # cc = ["marijn2huis@gmail.com", "pimduif@gmail.com", "t7133657@gmail.com"]
    # cc = []
    
    message = MIMEMultipart("alternative")
    message["Subject"] = "Birthday Message"
    message["From"] = sender_email
    message["To"] = ",".join(receiver_email)
    # message["Cc"] = ",".join(cc)

    body = MIMEText(html, "html")

    message.attach(body)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()
