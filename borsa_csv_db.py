import requests
import csv
import sqlite3

from datetime import datetime

from bs4 import BeautifulSoup

url = "http://bigpara.hurriyet.com.tr/borsa/hisse-fiyatlari/ayen-ayen-enerji-detay/"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

stock_name = soup.find("h1", {"class":"pageTitle mBot10"}).string
stock_price = soup.find("div", {"class":"hisseProcessBar mBot10"}).find("li", {"class":"type up"}).span.string
stock_value = soup.find("div", {"class":"hisseProcessBar mBot10"}).find_all("li")[2].b.string

#Güncel zaman bilgisi bölümü
time = datetime.now()

print("Tarih: {} \nHisse Seneti Adı: {} \nGüncel Hisse Fiyatı: {} \nHacim TL: {}".format(time, stock_name,stock_price,stock_value))

#CSV dosyasına yazım bölümü
file = open("borsa22.csv", "w+", encoding="utf-8" )
writer = csv.writer(file)
writer.writerow(("TARIH", "HISSE ADI", "GUNCEL FIYAT", "HACIM TL"))
writer.writerow([time, stock_name, stock_price, stock_value])
file.close()

#sqlite3 DB yazım bölümü
conn = sqlite3.connect('borsa.db')
c = conn.cursor()
c.execute("create table if not exists borsa (time text, name text, price real, value real)")
c.execute("insert into borsa values (?, ?, ? ,?)", (time, stock_name, stock_price, stock_value))
conn.commit()
conn.close()