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
        os.path.join(os.path.dirname(__file__), "src", "birthdays_pd.csv"),
        parse_dates=["birthday"],
    )

    bdays["birthday_year"] = bdays["birthday"].dt.year
    bdays["birthday_date"] = bdays["birthday"].dt.strftime("%m-%d")
    bdays["days_until_bday"] = bdays.apply(
        lambda bdays: calculate_days_until_bday(bdays["birthday"]), axis=1
    )

    bdays = bdays.sort_values("days_until_bday")

#we can do this in a smart way, need to use a dict later on, that will save us some lines.
    if any(bdays['days_until_bday'] == 0):
        email_list0 = bdays[bdays['0day'] == 1]['email'].to_list()
        bday_boy_day0 = bdays[bdays['days_until_bday'] == 0]['name'].squeeze() #i made it a str as a quick fix, now it definitely breaks for the twins
        email_list0.remove(bday_boy_day0) if bday_boy_day0 in email_list0 else None #remove bday boy, this probably breaks for the twins
        html_body_day0 = email_util.get_all_bdays_email_body_day(bdays, days = 0, bday_boy=bday_boy_day0)
        email_util.sending_email(html=html_body_day0, email_list=[x for x in email_list0 if str(x) != 'nan'])

    if any(bdays['days_until_bday'] == 1):
        email_list1 = bdays[bdays['1day'] == 1]['email'].to_list()
        bday_boy_day1 = bdays[bdays['days_until_bday'] == 1]['name'].squeeze() #i made it a str as a quick fix, now it definitely breaks for the twins
        email_list1.remove(bday_boy_day1) if bday_boy_day1 in email_list1 else None #remove bday boy, this probably breaks for the twins
        html_body_day1 = email_util.get_all_bdays_email_body_day(bdays, days = 1, bday_boy=bday_boy_day1)
        email_util.sending_email(html=html_body_day1, email_list=[x for x in email_list1 if str(x) != 'nan'])

    if any(bdays['days_until_bday'] == 7):
        email_list7 = bdays[bdays['7day'] == 1]['email'].to_list()
        bday_boy_day7 = bdays[bdays['days_until_bday'] == 7]['name'].squeeze() #i made it a str as a quick fix, now it definitely breaks for the twins
        email_list7.remove(bday_boy_day7) if bday_boy_day7 in email_list7 else None #remove bday boy, this probably breaks for the twins
        html_body_day7 = email_util.get_all_bdays_email_body_day(bdays, days = 7, bday_boy=bday_boy_day7)
        email_util.sending_email(html=html_body_day7, email_list=[x for x in email_list7 if str(x) != 'nan'])

    if datetime.now().day == 1:
        email_list_month = bdays['email'].to_list()
        html_body_month = email_util.get_all_bdays_email_body_month(bdays)
        email_util.sending_email(html=html_body_month, email_list=email_list_month)
   
if __name__ == "__main__":
    main()