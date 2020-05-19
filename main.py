html_doc ="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>İlk web sayfam</title>
</head>
<body>

    <h1 id="header">
        Python Kursu
    </h1>

    <div class="grup1">
        <h2>
            Programlama
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <div class="grup2">
        <h2>
            Modüller
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <div class="grup3">
        <h2>
            Django
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <img src="fred.jpg" alt="">

</body>
</html>
"""

import requests

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, "html.parser")

result = soup.prettify()

result = soup.title
result = soup.head
result = soup.body

result = soup.title.name
result = soup.title.string

result = soup.h1.string

result = soup.find_all("h2")
result = soup.find_all("h2")[1]

result = soup.div                                  #İlk div i çekmek için
result = soup.find_all("div")                      #Bütün div leri almak için 
result = soup.find_all("div")[1]                   #Bütün div leri bulup içinden ikinci div'i alır
result = soup.find_all("div")[1].ul                #Grup2 nin altındaki div in içindeki ul etiketine erişmek için
result = soup.find_all("div")[1].ul.li             #Grup2->2.div->ul->li erişmek için
result = soup.find_all("div")[1].ul.li.string      #Grup2->2.div->ul->li'nin içerigine erişmek için
result = soup.find_all("div")[1].ul.find_all("li") #Grup2->2.div->ul->li bütün li lere erişmek için


print(result)

