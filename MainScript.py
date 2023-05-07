from bs4 import BeautifulSoup
import pymongo
import requests
import re
import openpyxl
from openpyxl import load_workbook
import json

link = "https://www.startech.com.bd/laptop-notebook/laptop"

Laptops = ''
lapname = []
lapprice = []


def StarTech(l):
    html_texts = requests.get(l).text
    soup = BeautifulSoup(html_texts, 'lxml')
    
    laptop_Names = soup.find_all('div', class_='p-item-details')
    laptop_price = soup.find_all('div', class_='p-item-price')
    for ln in laptop_Names:
        for li in ln.find_all("h4"):
            name = li.text + " [Startech]"
            lapname.append(name)


    for ln in laptop_price:
        for li in ln.find_all("span"):
            price = li.text
            price =price.replace("৳", "") # do not need money sign since it will mess up future works
            price =price.replace(",", "") # do not need money sign since it will mess up future works
            price =price.replace("TBA", "0") # do not need money sign since it will mess up future works
            
            lapprice.append(price)

StarTech(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=2"
StarTech(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=3"
StarTech(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=4"
StarTech(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=5"
StarTech(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=6"
StarTech(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=7"
StarTech(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=8"
StarTech(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=9"
StarTech(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=10"
StarTech(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=11"
StarTech(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=12"
StarTech(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=13"
StarTech(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=14"
StarTech(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=15"
StarTech(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=16"
StarTech(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=17"
StarTech(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=18"
StarTech(link)
link= "https://www.startech.com.bd/laptop-notebook/laptop?page=19"
StarTech(link)

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
            price =price.replace("৳", "") # do not need money sign since it will mess up future works
            price =price.replace(",", "") # do not need money sign since it will mess up future works
            
            
            lapprice.append(price)

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


def RYANS(link):

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
        price =price.replace(",", "") # do not need money sign since it will mess up future works          
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


 

RYANS(link)
RYANS(link2)
RYANS(link3)
RYANS(link4)
RYANS(link5)
RYANS(link6)
RYANS(link7)
RYANS(link8)
RYANS(link9)
RYANS(link10)
RYANS(link11)
RYANS(link12)
RYANS(link13)
RYANS(link14)
RYANS(link15)
RYANS(link16)


x=slice(1120)
lapname=lapname[x]

lapprice=lapprice[x]



comb=dict(zip(lapname,lapprice))



myclient = pymongo.MongoClient("mongodb+srv://asiflogin:asif321@cluster0.scqzz.mongodb.net/?retryWrites=true&w=majority")
mydb = myclient["CSE425"]
mycol = mydb["laptopKinbo"] 

for x in range(0,1110):
    lapdict = {"name":lapname[int(x)],"price":int(lapprice[int(x)])}
    mycol.insert_one(lapdict)

print("Done!")
#final
