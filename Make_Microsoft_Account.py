from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import imaplib
from email.parser import Parser
import email
from bs4 import BeautifulSoup

fname = "futter"
name =  "account@futunlocked.com"
Pw = "Tester-7"
Ln = ("fut")
url = "https://signup.live.com/signup?uaid=f1c86ec9da134196a140659684e98757&lic=1"
browser = webdriver.Chrome('C:\webdrivers\chromedriver.exe')
browser.get(url)
wait = WebDriverWait(browser, timeout=10)


def New_account():
    count = 0
    while(count<101):
        count +=1
    else:
        print("its done")
New_account()

def MA_Firstpage():
    username = browser.find_element_by_id("MemberName")
    time.sleep(2)
    username.send_keys(name)
    password = browser.find_element_by_id("Password")
    time.sleep(2)
    password.send_keys(Pw)
    form = browser.find_element_by_id('iSignupAction')
    time.sleep(1.5)
    form.submit()
MA_Firstpage()

def MA_Secondpage():
    time.sleep(2)
    FirstName = browser.find_element_by_id("FirstName")
    time.sleep(2)
    FirstName.send_keys(fname)
    LastName = browser.find_element_by_id("LastName")
    time.sleep(1.5)
    LastName.send_keys(Ln)
    form = browser.find_element_by_id('iSignupAction')
    time.sleep(1.5)
    form.submit()
MA_Secondpage()

Name = ("label")
def MA_Thirdpage(browser, element_id, labels):
 try:
    (wait.until(EC.presence_of_element_located((By.ID, element_id))))
    print("found the id")
 except Exception as e:
    print(e)
 time.sleep(1.5)
 for label in labels:
      time.sleep(1.5)
      el = Select(browser.find_element_by_id(element_id))
      time.sleep(1.5)
      el.select_by_index(label)

MA_Thirdpage(browser, "Country",[158])
time.sleep(1.5)
MA_Thirdpage(browser, "BirthDay", [31])
time.sleep(1.5)
MA_Thirdpage(browser, "BirthMonth", [10])
time.sleep(1.5)
MA_Thirdpage(browser, "BirthYear", [22])
form = browser.find_element_by_id('iSignupAction')
time.sleep(1.5)
form.submit()

def EM_code():
    imap_host = 'mail.futunlocked.com'
    imap_user = '7account@futunlocked.com'
    imap_pass = 'Tester-7'

    ## open a connection
    imap = imaplib.IMAP4_SSL(imap_host)
    mail = imap
    ## login
    mail.login(imap_user, imap_pass)
    mail.select()

    result, data = mail.search(None, '(ALL)')
    ids = data[0]  # data is a list.
    id_list = ids.split()  # ids is a space separated string
    latest_email_id = id_list[-1]

    type, data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = data[0][1]

    ss = email.message_from_bytes(raw_email)
    p = Parser()
    email_message = p.parsestr(str(ss))
    html = str(email_message)
    time.sleep(15)
    soup = BeautifulSoup(html, "html.parser")
    bs = soup.find_all('span')
    time.sleep(2)
    s= print(bs[0].text)
    code = browser.find_element_by_id('VerificationCode')
    time.sleep(2)
    code.send_keys(s)
    form = browser.find_element_by_id('iSignupAction')
    time.sleep(1.5)
    form.submit()
EM_code()

