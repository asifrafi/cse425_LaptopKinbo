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


def ryans(link):

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


 

ryans(link)
ryans(link2)
ryans(link3)
ryans(link4)
ryans(link5)
ryans(link6)
ryans(link7)
ryans(link8)
ryans(link9)
ryans(link10)
ryans(link11)
ryans(link12)
ryans(link13)
ryans(link14)
ryans(link15)
ryans(link16)





print(lapname)
print(lapprice)

