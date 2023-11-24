import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


configure()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": os.getenv('STOCK_API_KEY'),
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
print(f"Data: {data}")

data_list = [value for (key, value) in data.items()]
print(f"Data List: {data_list}")
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(f"Yesterday's Closing Price: {yesterday_closing_price}")
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(f"Day Before Yesterday's Closing Price: {day_before_yesterday_closing_price}")
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
print(f"Difference of: {difference}")
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

percentage_difference = round((difference / float(day_before_yesterday_closing_price)) * 100)
print(f"Percentage Difference: {percentage_difference}")

if abs(percentage_difference) > 1:
    news_parameters = {
        "q": COMPANY_NAME,
        "apiKey": os.getenv('NEWS_API_KEY'),
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]

    three_articles = articles[:3]

    for article in three_articles:
        headline = article["title"].strip(":")
        description = article["description"]

        client = Client(os.getenv('ACCOUNT_SID'), os.getenv('AUTH_TOKEN'))
        message = client.messages \
            .create(
            body=f"{STOCK_NAME}: {up_down}{percentage_difference}%\n Headline: {headline}\n Brief: {description} ",
            from_=os.getenv('VIRTUAL_TWILIO_NUMBER'),
            to=os.getenv('VERIFIED_NUMBER')
        )
        print(message.status)
