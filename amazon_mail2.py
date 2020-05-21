import requests

from bs4 import BeautifulSoup

import smtplib

url = "https://www.amazon.co.uk/Sony-ILCE7KB-CE-Autofocus-Tiltable-Tru-Finder/dp/B00FWUDEEC"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

page = requests.get(url, headers = headers)

soup = BeautifulSoup(page.content, "html.parser")

title = soup.find(id="productTitle").get_text().strip()
price = soup.find(id="priceblock_ourprice").get_text()[1:]
price = float(price)

print(title)
print(price)

if (price < 760):
    send_mail()

def send_mail():
    server = smtplib.SMTP("smtp.gmail.com",587)   
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("my4192834@gmail.com","metinyilmaz1qaz3EDC")
    subject = "FIYAT DUSTU // "+title
    body = "Hemen Satin Al: "+url
    msg = f"Subject:{subject}\n\n{body}"
    server.sendmail("my4192834@gmail.com","my4192834@gmail.com",msg)
    print("Email gönderildi.")
    server.quit()
