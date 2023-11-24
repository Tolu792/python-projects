import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


configure()

LAT = 6.6314805
LONG = 3.4083004

parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": os.getenv('APP_ID'),
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

hourly_forcast = weather_data["hourly"][:12]

will_rain = False

for hour_data in hourly_forcast:
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(os.getenv('ACCOUNT_SID'), os.getenv('AUTH_TOKEN'))

    message = client.messages \
        .create(
        body="It's going to rain today. Bring an umbrella ☔",
        from_=os.getenv('TWILIO_NO'),
        to=os.getenv('PHONE_NO')
    )

    print(message.status)
