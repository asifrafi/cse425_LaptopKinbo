#RYANS

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


    laptop_Names = soup.find_all('p', class_='card-text p-0 m-0 grid-view-text')

    laptop_price = soup.find_all('p', class_='pr-text cat-sp-text pb-1')


   
    for ln in laptop_Names:

        for li in ln.find_all("a"):
            name = li.text + " [RYANS]"
            
            name = name.replace("...", "")
            
            lapname.append(name)



    for ln in laptop_price:
        price = ln.text
        price =price.replace("Tk", "")
        price =price.replace(" ", "")
        lapprice.append(price)
        

link = "https://www.ryanscomputers.com/category/laptop-all-laptop"
link2 ="https://www.ryanscomputers.com/category/laptop-all-laptop?page=2"
link3 ="https://www.ryanscomputers.com/category/laptop-all-laptop?page=3"
link4 ="https://www.ryanscomputers.com/category/laptop-all-laptop?page=4"
link5 ="https://www.ryanscomputers.com/category/laptop-all-laptop?page=5"
link6 ="https://www.ryanscomputers.com/category/laptop-all-laptop?page=6"
link7 ="https://www.ryanscomputers.com/category/laptop-all-laptop?page=7"
link8 ="https://www.ryanscomputers.com/category/laptop-all-laptop?page=8"
link9 ="https://www.ryanscomputers.com/category/laptop-all-laptop?page=9"
link10 ="https://www.ryanscomputers.com/category/laptop-all-laptop?page=10"
link11 ="https://www.ryanscomputers.com/category/laptop-all-laptop?page=11"
link12 ="https://www.ryanscomputers.com/category/laptop-all-laptop?page=12"
link13 ="https://www.ryanscomputers.com/category/laptop-all-laptop?page=13"
link14 ="https://www.ryanscomputers.com/category/laptop-all-laptop?page=14"
link15 ="https://www.ryanscomputers.com/category/laptop-all-laptop?page=15"
link16 ="https://www.ryanscomputers.com/category/laptop-all-laptop?page=16"


 

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





print(lapname)
print(lapprice)

