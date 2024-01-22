import os
from datetime import datetime, timedelta

import numpy as np
import pandas as pd


def get_names_string(df: pd.DataFrame):
    names_str = ", ".join([x for x in df["name"].values])
    if len(df["name"].values) >= 2:
        names_str = " and".join(names_str.rsplit(",", 1))
    return names_str


def main():
    bdays = pd.read_csv(
        os.path.join(os.path.dirname(__file__), "src", "birthdays.csv"),
        usecols=["name", "email", "birthday"],
        parse_dates=["birthday"],
    )

    bdays["birthday_year"] = bdays["birthday"].dt.year
    bdays["birthday_date"] = bdays["birthday"].dt.strftime("%m-%d")

    bdays["birthday_date_7"] = bdays["birthday"] - timedelta(days=7)
    bdays["birthday_date_1"] = bdays["birthday"] - timedelta(days=1)
    bdays["birthday_date_7"] = bdays["birthday_date_7"].dt.strftime("%m-%d")
    bdays["birthday_date_1"] = bdays["birthday_date_1"].dt.strftime("%m-%d")

    reminders = pd.read_csv(
        os.path.join(os.path.dirname(__file__), "src", "birthdays.csv"),
        usecols=["name", "email", "frequency"],
    )

    reminders["7_before"] = (
        reminders["frequency"].str.contains("1 week ervoor").astype(int)
    )
    reminders["1_before"] = (
        reminders["frequency"].str.contains("1 dag ervoor").astype(int)
    )
    reminders["0_before"] = reminders["frequency"].str.contains("Op de dag").astype(int)
    reminders = reminders.drop(columns=["frequency"])

    current_date = datetime.today().strftime("%m-%d")
    current_plus_1 = (datetime.today() + timedelta(days=1)).strftime("%m-%d")
    current_plus_7 = (datetime.today() + timedelta(days=7)).strftime("%m-%d")

    remind_0_df = bdays.loc[(bdays["birthday_date"] == current_date)].reset_index(
        drop=True
    )
    remind_1_df = bdays.loc[(bdays["birthday_date"] == current_plus_1)].reset_index(
        drop=True
    )
    remind_7_df = bdays.loc[(bdays["birthday_date"] == current_plus_7)].reset_index(
        drop=True
    )

    for index, row in reminders.iterrows():
        if row["7_before"]:
            print(
                f"Send email to {row['name']}, {row['email']}, with 7 day reminder for {get_names_string(remind_7_df)}"
            )
        if row["1_before"]:
            print(
                f"Send email to {row['name']}, {row['email']}, with 1 day reminder for {get_names_string(remind_1_df)}"
            )
        if row["0_before"]:
            print(
                f"Send email to {row['name']}, {row['email']}, with 0 day reminder for {get_names_string(remind_0_df)}"
            )


if __name__ == "__main__":
    print(__file__)
    main()
