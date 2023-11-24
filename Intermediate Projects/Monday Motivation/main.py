import smtplib
import datetime as dt
import random
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


configure()


now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 2:
    with open("quotes.txt", "r") as quotes:
        data = quotes.readlines()
        random_motivation = random.choice(data)
        print(random_motivation)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=os.getenv('my_email'), password=os.getenv('password'))
        connection.sendmail(from_addr=os.getenv('my_email'),
                            to_addrs="tolu792@yahoo.com",
                            msg=f"Subject:Monday Motivation\n\n{random_motivation}")
