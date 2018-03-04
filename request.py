import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.immobilienscout24.de/Suche/S-T/Haus-Kauf/Umkreissuche/Korntal_2dM_fcnchingen/70825/-64406/2104364/-/-/10/2,00-/-/EURO--430000,00?enteredFrom=one_step_search'
page = requests.get(url)
contents = page.content

soup = BeautifulSoup(contents,"lxml")
resultList = str( soup.find(string=re.compile("IS24.resultList")) )
resultList = resultList.strip()
print(type(resultList))
idx0 = resultList.find('resultListModel:')
idx1 = resultList.find('numberOfHits:')
print(idx0,idx1)

resultListModel = resultList[idx0:idx1] 
print(resultListModel)

'''
print(soup.find("script", attrs={"type":False}))

for link in soup.find_all('a'):
    print(link.get('href'))
'''
