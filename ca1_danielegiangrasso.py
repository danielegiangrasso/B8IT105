# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:22:18 2020

@author: 39333
"""

import unittest

import requests

from bs4 import BeautifulSoup

def getdata():    
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
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    cells = soup.find_all('td')
    print("Country,Confirmed Cases,Number of deaths, Death rate(%)", end='')
    cells = soup.find_all('td')
    dataset = []
    
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
                    dataset.append(value)
            except:
                print("An exception occurred")
             
    return dataset


def save_csv(dataset):

    csv_file = open('ca_daniele_giangrasso.csv', 'w')
    csv_file.write("Country,Confirmed Cases,Number of deaths, Death rate(%)\n")
    index = 0
    while index < len(dataset):
        csv_file.write('"{0}","{1}","{2}","{3}"\n'.format(
               dataset[index], dataset[index + 1], dataset[index + 2], dataset[index + 3]))
        index += 4
        
def main():
   dataset = getdata()   
   save_csv(dataset)
   
main()

#Because the table has 4 column I expect that every time
#I run the alghoritm and I divide the len of the data by 4
# it gives me 0 as result


class test_dataDownload(unittest.TestCase):
   
    def testModule(self):
        data = getdata()
        #print("\n\nthe number of data downloaded is:" , len(data))
        result = (len(data) % 4)
        self.assertEqual(0, result)
              

if __name__ == '__main__':
    unittest.main()
