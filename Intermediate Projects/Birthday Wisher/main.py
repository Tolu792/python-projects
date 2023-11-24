import random
from datetime import datetime
import pandas
import smtplib
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


configure()

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

if today_tuple in birthdays_dict:
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    birthday_person = birthdays_dict[today_tuple]

    with open(file_path) as letter:
        content = letter.read()
        modified_letter = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=os.getenv('MY_EMAIL'), password=os.getenv('PASSWORD'))
        connection.sendmail(from_addr=os.getenv('MY_EMAIL'),
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{modified_letter}")
