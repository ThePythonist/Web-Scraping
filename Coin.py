from bs4 import BeautifulSoup
import requests


def get_price(symbol):
    url = f"https://www.tgju.org/profile/{symbol}"
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    spans = soup.find_all('span', class_='value')
    price = spans[0].text.split()[0]
    return price


coins = ["rob", "nim", "sekee"]
prices = list(map(get_price, coins))
print(prices)
