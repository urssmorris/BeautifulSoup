import bs4 as bs
import urllib.request

# #Login
from requests import Session
from bs4 import BeautifulSoup as bs4

with Session() as s:
    site = s.get("https://intrahard.com/login")
    bs_content = bs4(site.content, "html.parser")
    login_data = {"usuario":"urssmorris@gmail.com","pwd":"elgranKathogas3", "login":"1"}
    s.post("https://intrahard.com/login",login_data)
    # home_page = s.get("https://intrahard.com/home/destacado/1")
    # print(home_page.content)

    
###########################

import requests

page = requests.get('https://intrahard.com/home/destacado/1')
# soup = bs.BeautifulSoup(page.text, 'html.parser')
soup = bs.BeautifulSoup(page.text, 'lxml')

#####basics

# print(soup.title.text)
# print(soup.a)
# print(soup.find_all('a'))

# for paragraph in soup.find_all('a'):
#     print(paragraph.text)

# print(soup.get_text())

################

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("./chromedriver", chrome_options=options)