#ThisIsForTechland
from bs4 import BeautifulSoup
import pymongo
import requests
import re
import openpyxl
from openpyxl import load_workbook

link = "https://www.techlandbd.com/shop-laptop-computer/brand-laptops"

Laptops = ''
lapname = []
lapprice = []


html_texts = requests.get(link).text
soup = BeautifulSoup(html_texts, 'lxml')
laptop_Names = soup.find_all('div', class_='name')
laptop_price = soup.find_all('div', class_='price')
#techland working
for ln in laptop_Names:
    for li in ln.find_all("a"):
        name = li.text + ' [TechLand]'
        lapname.append(name)

for ln in laptop_price:

    for li in ln.find_all("span"):
        price = li.text
        priceN =price.replace("৳", "") # do not need money sign since it will mess up future works
        lapprice.append(priceN)

print(lapname)
print(lapprice)