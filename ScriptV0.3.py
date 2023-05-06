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
laptop_Names = soup.find_all('div', class_='p-item-details')
laptop_price = soup.find_all('div', class_='p-item-price')
#test