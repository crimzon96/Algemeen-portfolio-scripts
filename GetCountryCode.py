from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import os
import json
import re
session = HTMLSession()
response = session.get('https://countryflags.io')
soup = BeautifulSoup(response.text, 'html.parser')
divs = soup.findAll('table')
folderName = "countryImageFlags"
def getCountry():
    country = {}
    for div in divs:
        row = div.findAll('tr')
        for code in row:
            countryName = ''
            if code.find('td') is not None:
                s = code.findAll('td')
                countryName = s[1].text
                countryIso = s[0].text
                country[countryName] = {'countryName': countryName, 'countryIso': countryIso, 'countryNumber' : '','countryFlag': 'https://www.countryflags.io/'+ str(code.find('td').text)+'/flat/24.png'}
                getImage = requests.get('https://www.countryflags.io/'+ str(code.find('td').text)+'/flat/24.png', stream=True)
                if not os.path.exists(folderName):
                    os.makedirs(folderName)
                if getImage.status_code == 200:
                    if not  os.path.exists(folderName + os.sep + countryName +'.png'):
                        with open(folderName + os.sep + countryName +'.png', 'wb') as f:
                            for chunk in getImage:
                                f.write(chunk)
                    else:
                        print('It already exist')
                else:
                    print('Not working' + str(getImage.status_code))

            else:
                print('Is None')
    with open('country_list.txt', 'w') as outfile:
        json.dump(country, outfile, sort_keys=True, indent=4,
                      ensure_ascii=False)
    return country
#getCountry()



def addCountryCode():
    countryNumber = ""
    get_CountryName = ""
    new_data_dict = {}
    response = requests.get('https://countrycode.org/')
    soup     =  BeautifulSoup(response.text, 'html.parser')
    get_Table = soup.find('tbody')
    get_Countrys = get_Table.find_all('a', href=True)
    for get_Country in get_Countrys:
        get_CountryName = get_Country.text
        for b in get_Table.findAll('tr'):
                match = re.search(get_CountryName, str(b))
                if match:
                    w= b.findAll('td')
                    countryNumber = '+'+w[1].text                   
        with open('country_list.txt') as json_file:
                data = json.load(json_file)
        for key, value in data.items():
            if get_CountryName == key:
                key, value.update({'countryNumber': countryNumber})
                new_list = key,value
                new_data=dict([new_list])
                new_data_dict.update(new_data)
                #print(d)
    with open('country_list.txt', 'w') as outfile:
        json.dump(new_data_dict, outfile, sort_keys=True, indent=4,
                        ensure_ascii=False)
    print(new_data_dict)
#addCountryCode()


imageDir= os.listdir(os.path.dirname(os.path.realpath(__file__)) + os.sep + 'countryImageFlags')
imagePath = os.path.dirname(os.path.realpath(__file__))+ os.sep + 'countryImageFlags'


def addCounryImage():
    getImage = ""
    new_data_dict = {}
    for getImage in imageDir:  
        with open('country_list.txt') as json_file:
            data = json.load(json_file)
            for key, value in data.items():
                if key+'.png' == getImage:
                    key, value.update({'countryFlag': imagePath + os.sep + getImage})
                    new_list = key,value
                    new_data=dict([new_list])
                    new_data_dict.update(new_data)
    with open('country_list.txt', 'w') as outfile:
        json.dump(new_data_dict, outfile, sort_keys=True, indent=4,
                        ensure_ascii=False)
    #print(new_data_dict)
#addCounryImage()

def addCountryLanguage():
    language_list = []
    response = requests.get('https://en.wiktionary.org/wiki/Index:All_languages')
    soup =  BeautifulSoup(response.text, 'html.parser')
    get_table = soup.find('table')
    get_tr = get_table.findAll('tr')
    for get_href_text in get_tr:
       get_td = get_href_text.find('td')
       if get_td is not None :
           language_list.append(tuple([get_td.text.strip(), get_td.text.strip()]))
           
       else:
           pass
    mytuple = language_list
    #with open('language_list.txt', 'a') as f:
        #f.write(str(mytuple))
    return mytuple
addCountryLanguage()
    #for get_language in l

def country_list():
    country_list = []

    with open('country_list.txt') as f:
        data = json.load(f)
    for k,v in data.items():
        country_list.append(tuple([v['countryName'],v['countryName']]))
        #country_list.append(v['countryName'])
        #country_list.append(k['countryName'])
    mytuple = tuple(country_list)
    return mytuple

#country_list()
