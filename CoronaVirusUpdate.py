# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 18:45:19 2020

@author: danie
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 15:46:33 2020

@author: danie
"""


import requests

from bs4 import BeautifulSoup

headers = {
    'authority': 'www.statista.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'referer': 'https://www.google.com/',
    'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'STATSESSID=klqgfufi37clc25vc4q161kber; abtest=2; _ga=GA1.2.2040521487.1585489064; _gid=GA1.2.244288196.1585489064; _fbp=fb.1.1585489064735.258681423; cookiesNotificationHidden=true; ViewInfographicCount=3; lastStatisticId=1105914; lastStatisticUrltitle=coronavirus-death-rates-worldwide; lastStatisticFree=1; lastStatisticVisit=O^%^3A8^%^3A^%^22DateTime^%^22^%^3A3^%^3A^%^7Bs^%^3A4^%^3A^%^22date^%^22^%^3Bs^%^3A26^%^3A^%^222020-03-29+18^%^3A16^%^3A10.112472^%^22^%^3Bs^%^3A13^%^3A^%^22timezone_type^%^22^%^3Bi^%^3A3^%^3Bs^%^3A8^%^3A^%^22timezone^%^22^%^3Bs^%^3A3^%^3A^%^22UTC^%^22^%^3B^%^7D; lastStatisticType=table; _gat_UA-76064938-1=1; _dc_gtm_UA-76064938-1=1',
}

response = requests.get('https://www.statista.com/statistics/1105914/coronavirus-death-rates-worldwide/', headers=headers)



#print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')

#print(soup.prettify())

#print (soup.title.string)
 
cells = soup.find_all('td')


#print(cells)


cells = soup.find_all('td')

value = 0

for cell in cells:
    for content in cell.contents:
        value = str(content).strip().replace('\n', '')
        try:
            if value[0] != "<":                
                if len(value) == 0:
                    print('"0"', end=',')
                elif value[0].lower() in 'abcdefghijklmnopqrstuvwxyz':
                    print('\n' + value, end=',')
                else:
                   print('"' + value + '"', end=',')
        except:
            break
            
