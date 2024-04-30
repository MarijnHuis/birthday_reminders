import os
from datetime import datetime
import pandas as pd

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
    print(bdays)

if __name__ == "__main__":
    main()
