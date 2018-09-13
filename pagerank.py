import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
options.add_argument('--no-sandbox') # Bypass OS security model
options.add_argument('start-maximized') #
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe', chrome_options=options)
#driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe')
wait = WebDriverWait(driver, 10)


def get_pagerank(browser, domainname, keyword):
    page_rank_dict   = {}
    page_rank_dict['pagerankdict'] = {}
    try:
        url = "https://www.google.com/"
        driver.get(url)
        google_search_field =wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="lst-ib"]')))
        if google_search_field:
            google_search_field.send_keys(keyword)
        else:
            print('Google changed his search_field')
        google_search_button = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="tsf"]/div[2]/div[3]/center/input[1]')))
        if google_search_button:
            google_search_button.submit()
        else:
            print('Google changed his search_button')
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        google_link =soup.findAll('h3', attrs={'class': 'r' })
        count =  0
        for link in google_link:
            if link.find('a',href=True):
                search_href = link.find('a', href=True)
                count += 1
                start_clean_Url = re.sub('(https:\/\/www.)|(http:\/\/www)|(www)|(https?:|)\/\/|(http)', '',
                                         search_href.get('href'))
                start_clean_Url = re.sub('\/.*', '', start_clean_Url)
                cleaned_Url = "https://" + start_clean_Url + "/"
                if page_rank_dict:
                    page_rank_dict.update({count: cleaned_Url})
                else:
                    pass
            else:
                pass
    except:
        url = "https://www.google.com/"
        driver.get(url)
        google_search_field = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="lst-ib"]')))
        time.sleep(10)
        if google_search_field:
            google_search_field.send_keys(keyword)
        else:
            print('Google changed his search_field')
        google_search_button = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="tsf"]/div[2]/div[3]/center/input[1]')))
        time.sleep(10)
        if google_search_button:
            google_search_button.submit()
        else:
            print('Google changed his search_button')
            time.sleep(10)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        google_link = soup.findAll('h3', attrs={'class': 'r'})
        count = 0
        for link in google_link:
            if link.find('a', href=True):
                search_href = link.find('a', href=True)
                count += 1
                start_clean_Url = re.sub('(https:\/\/www\W)|(http:\/\/www\W)|(www\W)|(http:\/\/)|(https:\/\/\W)|(www\W)|(htpp:\/\/)|(https:\/\/)|(http:\/\/www\W)', '', search_href.get('href'))
                start_clean_Url = re.sub('\/.*', '', start_clean_Url)
                cleaned_Url = "https://" + start_clean_Url + "/"
                if page_rank_dict:
                    page_rank_dict.update({count: cleaned_Url})
                else:
                    pass
            else:
                pass
    getvalue = {k: v for k, v in page_rank_dict.items() if v}
    return getvalue

