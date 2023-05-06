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


def techland(l):
    html_texts = requests.get(link).text
    soup = BeautifulSoup(html_texts, 'lxml')
    laptop_Names = soup.find_all('div', class_='name')
    laptop_price = soup.find_all('div', class_='price')
    for ln in laptop_Names:
        for li in ln.find_all("a"):
            name = li.text + " [TechLand]"
            lapname.append(name)

    for ln in laptop_price:

        for li in ln.find_all("span"):
            price = li.text
            priceN =price.replace("৳", "") # do not need money sign since it will mess up future works
            
            lapprice.append(priceN)

link= "https://www.techlandbd.com/shop-laptop-computer/brand-laptops"
techland(link)
link= "https://www.techlandbd.com/shop-laptop-computer/brand-laptops?page=2"
techland(link)
link= "https://www.techlandbd.com/shop-laptop-computer/brand-laptops?page=3"
techland(link)
link= "https://www.techlandbd.com/shop-laptop-computer/brand-laptops?page=4"
techland(link)
link= "https://www.techlandbd.com/shop-laptop-computer/brand-laptops?page=5"
techland(link)
link= "https://www.techlandbd.com/shop-laptop-computer/brand-laptops?page=6"
techland(link)
link= "https://www.techlandbd.com/shop-laptop-computer/brand-laptops?page=7"
techland(link)
link= "https://www.techlandbd.com/shop-laptop-computer/brand-laptops?page=8"
techland(link)
link= "https://www.techlandbd.com/shop-laptop-computer/brand-laptops?page=9"
techland(link)
link= "https://www.techlandbd.com/shop-laptop-computer/brand-laptops?page=10"
techland(link)
link= "https://www.techlandbd.com/shop-laptop-computer/brand-laptops?page=11"
techland(link)
link= "https://www.techlandbd.com/shop-laptop-computer/brand-laptops?page=12"
techland(link)
link= "https://www.techlandbd.com/shop-laptop-computer/brand-laptops?page=13"
techland(link)
link= "https://www.techlandbd.com/shop-laptop-computer/brand-laptops?page=14"
techland(link)
link= "https://www.techlandbd.com/shop-laptop-computer/brand-laptops?page=15"
techland(link)
link= "https://www.techlandbd.com/shop-laptop-computer/brand-laptops?page=16"
techland(link)
link= "https://www.techlandbd.com/shop-laptop-computer/brand-laptops?page=17"
techland(link)
link= "https://www.techlandbd.com/shop-laptop-computer/brand-laptops?page=18"
techland(link)
link= "https://www.techlandbd.com/shop-laptop-computer/brand-laptops?page=19"
link= "https://www.techlandbd.com/shop-laptop-computer/brand-laptops?page=20"
techland(link)
link= "https://www.techlandbd.com/shop-laptop-computer/brand-laptops?page=21"
techland(link)
link= "https://www.techlandbd.com/shop-laptop-computer/brand-laptops?page=22"
techland(link)
link= "https://www.techlandbd.com/shop-laptop-computer/brand-laptops?page=23"
techland(link)


#print(lapname)
#print(lapprice)
x=slice(440)
lapprice =lapprice[x]
print(len(lapname))
print(len(lapprice))
print(lapprice[10])