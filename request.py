import requests
from bs4 import BeautifulSoup
import re

# url = 'https://www.immobilienscout24.de/Suche/S-T/Haus-Kauf/Umkreissuche/Korntal_2dM_fcnchingen/70825/-64406/2104364/-/-/10/2,00-/-/EURO--430000,00?enteredFrom=one_step_search'
url = 'https://www.immobilienscout24.de/Suche/S-T/Haus-Kauf/Umkreissuche/Stuttgart_2dWeilimdorf/-/-64234/2101233/-/1276001039003/10/3,00-/-/EURO--500000,00/-/false/-/-/-/-/-/-/-/-/1970-?saveSearchId=73613769&enteredFrom=saved_search'
page = requests.get(url)
contents = page.content

soup = BeautifulSoup(contents,"lxml")
# locate the result list
resultList = str( soup.find(string=re.compile("IS24.resultList")) )
resultList = resultList.strip()

# locate resultListModel
idx0 = resultList.find('resultListModel:')
idx1 = resultList.find('numberOfHits:')
resultListModel = resultList[idx0:idx1] 
# locate resultListEntry
idx0 = resultListModel.find('resultlistEntry')
resultListEntry = resultListModel[idx0:]
# number of estates found 
numEstate = resultListEntry.count('realEstateId')
# estates in a list
estates = resultListEntry.split('realEstateId')
del estates[0]

for estate in estates:
    idx_title = estate.find('\"title\"')
    idx_addr  = estate.find('\"address\"')
    idx_addre = estate.find('\"companyWideCustomerId\"')
    idx_price = estate.find('\"price\"')
    idx_pricee= estate.find('\"realEstateTags\"')
    print(estate[idx_title: idx_addr])
    print(estate[idx_addr: idx_addre])
    print(estate[idx_price: idx_pricee])
    print('=====================================')

'''
print(soup.find("script", attrs={"type":False}))

for link in soup.find_all('a'):
    print(link.get('href'))
'''
