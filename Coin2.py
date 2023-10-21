from selenium import webdriver
from selenium.webdriver.common.by import By


def get_price(symbol):
    driver = webdriver.Chrome()
    driver.get(f"https://tgju.org/profile/{symbol}")
    paragraphs = driver.find_elements(By.CLASS_NAME, "value")
    # for i in paragraphs:
    #     print(i.text)
    price = str(paragraphs[0].text).split()[0]
    return price


print(get_price("rob"))
# driver.quit()
coins = ["rob", "nim", "sekee"]
prices = list(map(get_price, coins))
print(prices)
