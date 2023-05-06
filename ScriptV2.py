from bs4 import BeautifulSoup
import pymongo
import requests
import re
import openpyxl
from openpyxl import load_workbook

link = "https://www.startech.com.bd/laptop-notebook/laptop"

Laptops = ''
lapname = []
lapprice = []


def soups(l):
    html_texts = requests.get(l).text
    soup = BeautifulSoup(html_texts, 'lxml')
    
    laptop_Names = soup.find_all('div', class_='p-item-details')
    laptop_price = soup.find_all('div', class_='p-item-price')
    for ln in laptop_Names:
        for li in ln.find_all("h4"):
            name = li.text
            lapname.append(name)


    for ln in laptop_price:
        for li in ln.find_all("span"):
            price = li.text
            lapprice.append(price)

soups(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=2"
soups(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=3"
soups(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=4"
soups(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=5"
soups(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=6"
soups(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=7"
soups(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=8"
soups(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=9"
soups(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=10"
soups(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=11"
soups(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=12"
soups(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=13"
soups(link)

print(lapname)
print(lapprice)
