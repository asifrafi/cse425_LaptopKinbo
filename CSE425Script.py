from bs4 import BeautifulSoup
import pymongo
import requests
import re
import openpyxl
from openpyxl import load_workbook
link = "https://www.startech.com.bd/laptop-notebook/laptop"

html_texts = requests.get(link).text
soup = BeautifulSoup(html_texts, 'lxml')

laptop_Names = soup.find_all('div', class_='p-item-details')
laptop_price = soup.find_all('div', class_='p-item-price')

Laptops = ''
lapname = []
lapprice = []
for ln in laptop_Names:
    for li in ln.find_all("h4"):
        name = li.text
        lapname.append(name)


for ln in laptop_price:
    for li in ln.find_all("span"):
        price = li.text
        lapprice.append(price)

link = "https://www.startech.com.bd/laptop-notebook/laptop?page=2"
html_texts = requests.get(link).text
soup = BeautifulSoup(html_texts, 'lxml')

for ln in laptop_Names:
    for li in ln.find_all("h4"):
        name = li.text
        lapname.append(name)


for ln in laptop_price:
    for li in ln.find_all("span"):
        price = li.text
        lapprice.append(price)

def soups(l):
    html_texts = requests.get(l).text
    soup = BeautifulSoup(html_texts, 'lxml')
    for ln in laptop_Names:
        for li in ln.find_all("h4"):
            name = li.text
            lapname.append(name)


    for ln in laptop_price:
        for li in ln.find_all("span"):
            price = li.text
            lapprice.append(price)




print(lapname)
print(lapprice)
