import urllib.request
from urllib.request import urljoin,urlopen
from bs4 import BeautifulSoup
import requests
import re
import time
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
starturl = "http://www.websiteseocheck.nl/overzicht.php"
headers={'User-Agent':user_agent,}
response = requests.get(starturl, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")




def  link_getter():
    value = []
    for tr in soup.find_all('tr')[1:]:
        tds = tr.find_all('td')
        lead = tds[1].text
        lead = re.sub("\/.*", "", lead)
        lead_url = "http://" + lead + "/"
        value.append(lead_url)


    return value

print(link_getter())





def wordpress_readme_Check():
    wp_readme_lead = link_getter()
    for wp in wp_readme_lead:
        try:
            r = requests.get(wp + 'readme.html', headers=headers)
            bsObj = BeautifulSoup(r.text, "html.parser")
            b = bsObj.title.string
            b = re.sub('\W\W.ReadMe', '', b)
            if b == "WordPress":
                print(wp + " is a Wordpress site")
        except:
           pass
           print(wp + " Is not a Wordpress site")


wordpress_readme_Check()






def wordpress_readme_Check():
    wp_readme_lead = link_getter()
    for wp in wp_readme_lead:
        r = requests.get(wp, headers=headers)
        bsObj = BeautifulSoup(r.text, "html.parser")
        b = bsObj.title.string
        b = re.sub('\W\W.ReadMe', '', b)
        if b == "WordPress":
            print(b)
wordpress_readme_Check()

wordpress_readme_Check()

def makeLeadUrl():
    lead = link_getter()
    lu_list = []
    for obj in lead:
        lead_url = "http://" + obj
        lu_list.append(lead_url)
    return lu_list

makeLeadUrl()

def wordpressCheck():
    lead = makeLeadUrl()
    for lead_website in lead:
        response      =  requests.get(lead_website)
        bsObj = BeautifulSoup(response.text, "html.parser")
        line = "WordPress"
        WordPress_meta_tag = bsObj.find("meta", attrs={'name': 'generator', 'content': 'WordPress 4.8.2'})
        print(WordPress_meta_tag)
        if WordPress_meta_tag == "WordPress 4.8.2":
            time.sleep(15)
            WordPress_tag      = WordPress_meta_tag["content"]
            WordPress_tag      = re.sub("\d|\W", "", WordPress_tag)
            print(WordPress_tag)
            searchObj          = re.search(r"[a-zA-Z]+\w", line, flags=0)
            if searchObj.group()  == WordPress_tag:
                print(lead_website)
                print("is wordpress")
            else:
                print(lead_website)
                print("no wordpress")
        else:
            print("NOT A WORDPRESS SITE")

    print("Got all websites")

wordpressCheck()


print(checker)
response = requests.get(checker)
bsObj = BeautifulSoup(response.text, "html.parser")



rL = "{}".format("\n"'http://'.join(wp_url))
rL = re.sub("(^[a-zA-Z0-9\-\.]+\W+)|[^/]+$", "", rL)
print(rL)

response = requests.get(rL, headers=headers)
print(response)


# alles achter de / ^[^/]+
#verwijder de /

# verwijder alles voor de string ^.*[\\\/]