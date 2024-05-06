import os
from datetime import datetime
import pandas as pd
import email_util

def calculate_days_until_bday(original_date: datetime):
    now = datetime.now()
    # check if birthday is today
    if now.day == original_date.day and now.month == original_date.month:
        return 0

    delta1 = datetime(now.year, original_date.month, original_date.day)
    delta2 = datetime(now.year + 1, original_date.month, original_date.day)
    pass
    return ((delta1 if delta1 > now else delta2) - now).days + 1

def main():
    bdays = pd.read_csv(
        os.path.join(os.path.dirname(__file__), "data", "birthdays.csv"),
        parse_dates=["birthday"],
    )

    bdays["birthday_year"] = bdays["birthday"].dt.year
    bdays["birthday_date"] = bdays["birthday"].dt.strftime("%m-%d")
    bdays["days_until_bday"] = bdays.apply(
        lambda bdays: calculate_days_until_bday(bdays["birthday"]), axis=1
    )

    bdays = bdays.sort_values("days_until_bday")

    day_list = [0, 1, 7]
    for i in day_list:
        if any(bdays['days_until_bday'] == i):
            email_list = bdays[bdays[f'{i}day'] == 1]['email'].to_list()
            bday_boy = bdays[bdays['days_until_bday'] == i]['name'].to_list()
            bday_boy_email = bdays[bdays['days_until_bday'] == i]['email'].to_list()
            email_list_reduced = [x for x in email_list if x not in bday_boy_email]
            html_body = email_util.get_all_bdays_email_body(bdays, days = i, bday_boy=bday_boy)
            email_util.sending_email(html=html_body, email_list=[x for x in email_list_reduced if str(x) != 'nan'])
    
    if datetime.now().day == 1:
        email_list_month = bdays['email'].to_list()
        html_body_month = email_util.get_all_bdays_email_body_month(bdays)
        email_list_reduced = [x for x in email_list_month if str(x) != 'nan']
        email_util.sending_email(html=html_body_month, email_list=email_list_reduced)
   
if __name__ == "__main__":
    main()