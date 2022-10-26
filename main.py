from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
import os

URL = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
headers = {
      "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}


response = requests.get(url=URL, headers=headers)
amazon_page = response.text

soup = BeautifulSoup(amazon_page, "lxml")

price = soup.find(name="span", class_="a-price")
price_text = price.getText()
price_split = price_text.split("$")
price_number = float(price_split[1])

if price_number < 200:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user="codingpractice123321@gmail.com",  password=os.environ["APP_PASS"])
        connection.sendmail(
              from_addr="codingpractice123321@gmail.com",
              to_addrs="claudiachurch00@gmail.com",
              msg="Buy pot"
        )



