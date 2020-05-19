import requests
import csv

from bs4 import BeautifulSoup

url = "http://bigpara.hurriyet.com.tr/borsa/hisse-fiyatlari/ayen-ayen-enerji-detay/"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

name = soup.find("h1", {"class":"pageTitle mBot10"}).string
price = soup.find("div", {"class":"hisseProcessBar mBot10"}).find("li", {"class":"type up"}).span.string
value = soup.find("div", {"class":"hisseProcessBar mBot10"}).find_all("li")[2].b.string

print("Hisse Seneti Adı: {} \nGüncel Hisse Fiyatı: {} \nHacim TL: {}".format(name,price,value))

file = open("borsa22.csv", "w+", encoding="utf-8" )
writer = csv.writer(file)
writer.writerow(("HISSE ADI", "GUNCEL FIYAT", "HACIM TL"))
writer.writerow([name, price, value])
 
file.close()