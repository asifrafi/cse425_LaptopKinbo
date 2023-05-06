from bs4 import BeautifulSoup
import pymongo
import requests
import re
import openpyxl

from openpyxl import load_workbook

Laptops = '' 
lapname = []
lapprice = []


def selectName(link):

    html_texts = requests.get(link).text

    soup = BeautifulSoup(html_texts, 'lxml')


    laptop_Names = soup.find_all('div', class_='p-item-details')

    laptop_price = soup.find_all('div', class_='p-item-price')


    laptop_Names.pop()

    laptop_Names.pop()

   
    for ln in laptop_Names:

        for li in ln.find_all("h4"):
            name = li.text
            lapname.append(name)



    for ln in laptop_price:

        for li in ln.find_all("span"):
            price = li.text
            lapprice.append(price)

link = "https://www.startech.com.bd/laptop-notebook/laptop"
link2 ="https://www.startech.com.bd/laptop-notebook/laptop?page=2"
link3 ="https://www.startech.com.bd/laptop-notebook/laptop?page=3"
link4 ="https://www.startech.com.bd/laptop-notebook/laptop?page=4"
link5 ="https://www.startech.com.bd/laptop-notebook/laptop?page=5"
link6 ="https://www.startech.com.bd/laptop-notebook/laptop?page=6"
link7 ="https://www.startech.com.bd/laptop-notebook/laptop?page=7"
link8 ="https://www.startech.com.bd/laptop-notebook/laptop?page=8"
link9 ="https://www.startech.com.bd/laptop-notebook/laptop?page=9"
link10 ="https://www.startech.com.bd/laptop-notebook/laptop?page=10"
link11 ="https://www.startech.com.bd/laptop-notebook/laptop?page=11"
link12 ="https://www.startech.com.bd/laptop-notebook/laptop?page=12"
link13 ="https://www.startech.com.bd/laptop-notebook/laptop?page=13"
link14 ="https://www.startech.com.bd/laptop-notebook/laptop?page=14"
link15="https://www.startech.com.bd/laptop-notebook/laptop?page=15"
link16 ="https://www.startech.com.bd/laptop-notebook/laptop?page=16"
link17 ="https://www.startech.com.bd/laptop-notebook/laptop?page=17"
link18 ="https://www.startech.com.bd/laptop-notebook/laptop?page=18"
link19 ="https://www.startech.com.bd/laptop-notebook/laptop?page=19"
link20 ="https://www.startech.com.bd/laptop-notebook/laptop?page=20"
link21 ="https://www.startech.com.bd/laptop-notebook/laptop?page=21"
link22 ="https://www.startech.com.bd/laptop-notebook/laptop?page=22"
link23 ="https://www.startech.com.bd/laptop-notebook/laptop?page=23"
link24 ="https://www.startech.com.bd/laptop-notebook/laptop?page=24"
link25 ="https://www.startech.com.bd/laptop-notebook/laptop?page=25"
link26 ="https://www.startech.com.bd/laptop-notebook/laptop?page=26"
link27 ="https://www.startech.com.bd/laptop-notebook/laptop?page=27"
link28 ="https://www.startech.com.bd/laptop-notebook/laptop?page=28"
link29 ="https://www.startech.com.bd/laptop-notebook/laptop?page=29"
link30 ="https://www.startech.com.bd/laptop-notebook/laptop?page=30"
link31 ="https://www.startech.com.bd/laptop-notebook/laptop?page=31"
link32 ="https://www.startech.com.bd/laptop-notebook/laptop?page=32"
link33 ="https://www.startech.com.bd/laptop-notebook/laptop?page=33"
link34 ="https://www.startech.com.bd/laptop-notebook/laptop?page=34"


 

selectName(link)
selectName(link2)
selectName(link3)
selectName(link4)
selectName(link5)
selectName(link6)
selectName(link7)
selectName(link8)
selectName(link9)
selectName(link10)
selectName(link11)
selectName(link12)
selectName(link13)
selectName(link14)
selectName(link15)
selectName(link16)
selectName(link17)
selectName(link18)
selectName(link19)
selectName(link20)
selectName(link21)
selectName(link22)
selectName(link23)
selectName(link24)
selectName(link25)
selectName(link26)
selectName(link27)
selectName(link28)
selectName(link29)
selectName(link30)
selectName(link31)
selectName(link32)
selectName(link33)
selectName(link34)




print(lapname)
print(lapprice)

