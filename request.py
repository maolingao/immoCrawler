import requests
from bs4 import BeautifulSoup
import re

# url = 'https://www.immobilienscout24.de/Suche/S-T/Haus-Kauf/Umkreissuche/Korntal_2dM_fcnchingen/70825/-64406/2104364/-/-/10/2,00-/-/EURO--430000,00?enteredFrom=one_step_search'
url = 'https://www.immobilienscout24.de/Suche/S-T/Haus-Kauf/Umkreissuche/Stuttgart_2dWeilimdorf/-/-64234/2101233/-/1276001039003/10/3,00-/-/EURO--500000,00/-/false/-/-/-/-/-/-/-/-/1970-?saveSearchId=73613769&enteredFrom=saved_search'
page = requests.get(url)
contents = page.content

soup = BeautifulSoup(contents,"lxml")

containers = soup.findAll("div", {"class":"grid-item result-list-entry__data-container"})

filename = "immoList.csv"
f = open(filename, "w")
header = "title, address, price, footage, numOfRooms, estate\n"
f.write(header)

for container in containers :
    title = container.div.a.text
    divAddr = container.findAll("div",{"class":"result-list-entry__address"})
    addr = divAddr[0].a.text
    divPremiumCriteria = container.findAll("dl", {"class":"grid-item result-list-entry__primary-criterion "})
    divPrice = divPremiumCriteria[0]
    divFootage = divPremiumCriteria[1]
    divNumRooms = divPremiumCriteria[2]
    price = divPrice.dd.text
    footage = divFootage.dd.text
    numRooms = divNumRooms.dd.text
    dlEstate = container.findAll("dl", {"class":"grid-item result-list-entry__primary-criterion gt3" })
    estate = dlEstate[0].dd.text

    f.write(title.replace(",","-") + "," + addr.replace(",","-") + "," + price.replace(",","-") + "," + footage.replace(",","-") + "," + numRooms.replace(",","-") + "," + estate.replace(",","-") + "\n")

f.close()
