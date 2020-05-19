import requests

from bs4 import BeautifulSoup

url = "https://www.amazon.co.uk/Sony-ILCE7KB-CE-Autofocus-Tiltable-Tru-Finder/dp/B00FWUDEEC"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

page = requests.get(url, headers = headers)

soup = BeautifulSoup(page.content, "html.parser")

title = soup.find(id="productTitle").get_text().strip()
price = soup.find(id="priceblock_ourprice").get_text()

print(title)
print(price)