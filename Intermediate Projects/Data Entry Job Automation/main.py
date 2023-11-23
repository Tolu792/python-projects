from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7"
}

url = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C" \
      "%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56825534228516%2C%22east%22%3A-122" \
      ".29840365771484%2C%22south%22%3A37.69763971693579%2C%22north%22%3A37.85286271598516%7D%2C%22regionSelection%22" \
      "%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value" \
      "%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A" \
      "%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C" \
      "%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A3000" \
      "%7D%2C%22price%22%3A%7B%22max%22%3A559862%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%2C" \
      "%22usersSearchTerm%22%3A%22San%20Francisco%20CA%22%7D"

response = requests.get(url=url, headers=header)
response.raise_for_status()
html_website = response.text
# print(html_website)

soup = BeautifulSoup(html_website, "html.parser")
links = soup.find_all(name="a", class_="StyledPropertyCardDataArea-c11n-8-84-3__sc-yipmu-0 jnnxAW property-card-link")
list_links = [link.get("href") for link in links]
modified_links = []

for link in list_links:
    if "http" not in link:
        modified_links.append(f"https://www.zillow.com{link}")
    else:
        modified_links.append(link)

print(modified_links)

prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1 iMKTKr")
list_prices = [price.getText().split()[0].replace("+", "").replace("/mo", "") for price in prices]
print(list_prices)

addresses = soup.find_all(name="address")
list_addresses = [address.getText() for address in addresses]
print(list_addresses)

driver = webdriver.Chrome()
for index in range(len(list_addresses)):
    driver.get(
        "https://docs.google.com/forms/d/e/1FAIpQLScA7KU24eaEBVee2dsZ6pp_YGphXS24iWwUNQz1vgIbVRZKOQ/viewform?usp"
        "=sf_link")
    sleep(2)

    address_of_property = driver.find_element(by=By.XPATH,
                                              value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div['
                                                    '2]/div/div[1]/div/div[1]/input')
    price_of_property = driver.find_element(by=By.XPATH,
                                            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div['
                                                  '1]/div/div[1]/input')
    link_of_property = driver.find_element(by=By.XPATH,
                                           value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div['
                                                 '1]/div/div[1]/input')
    submit_button = driver.find_element(by=By.CLASS_NAME, value="NPEfkd")

    address_of_property.send_keys(list_addresses[index])
    price_of_property.send_keys(list_prices[index])
    link_of_property.send_keys(modified_links[index])
    submit_button.click()
    sleep(5)
