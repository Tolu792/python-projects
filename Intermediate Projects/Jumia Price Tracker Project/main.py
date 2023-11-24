import smtplib
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


configure()

BUY_PRICE = 500000

url = "https://www.jumia.com.ng/sony-ps5-playstation-5-console-bundle-77522653.html"
response = requests.get(url)
response.raise_for_status()
html_website = response.text
# print(html_website)

soup = BeautifulSoup(html_website, "html.parser")
product = soup.find(name="h1", class_="-fs20 -pts -pbxs").getText()
price = soup.find(name="span", dir="ltr").getText()
price_split = price.split()[1]
price_formatted = price_split.replace(",", "")
price_as_int = int(price_formatted)

print(product)
print(price)

if price_as_int < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=os.getenv('my_email'), password=os.getenv('password'))
        connection.sendmail(from_addr=os.getenv('my_email'),
                            to_addrs="tolu792@yahoo.com",
                            msg=f"Subject:Jumia Price Alert!\n\n{product} is now {price}\n{url}".encode("utf-8"))
