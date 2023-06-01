from bs4 import BeautifulSoup
import pymongo
import requests
import re
import openpyxl
from openpyxl import load_workbook
import json
#script_to_run
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


x=slice(300)
lapname=lapname[x]

lapprice=lapprice[x]



comb=dict(zip(lapname,lapprice))



myclient = pymongo.MongoClient("mongodb+srv://asiflogin:asif321@cluster0.scqzz.mongodb.net/?retryWrites=true&w=majority")
mydb = myclient["CSE425"]
mycol = mydb["laptopKinbo"] 

for x in range(0,300):
    lapdict = {"name":lapname[int(x)],"price":int(lapprice[int(x)])}
    mycol.insert_one(lapdict)

print("Done!")
#final