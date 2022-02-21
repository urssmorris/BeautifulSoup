import bs4 as bs
import urllib.request

# #Login
# from requests import Session
# from bs4 import BeautifulSoup as bs

# with Session() as s:
#     site = s.get("https://intrahard.com/login")
#     bs_content = bs(site.content, "html.parser")
#     login_data = {"usuario":"urssmorris@gmail.com","pwd":"elgranKathogas3", "login":"1"}
#     s.post("https://intrahard.com/login",login_data)
    # home_page = s.get("https://intrahard.com/home/destacado/1")
    # print(home_page.content)
###########################

import requests
from bs4 import BeautifulSoup


username = 'urssmorris@gmail.com'
password = 'elgranKathogas3'
login = '1'
values = {'usuario': username, 'pwd': password, "login": login}

session = requests.session()

login_url = 'https://intrahard.com/login'
url = 'https://intrahard.com/home/destacado/1'

result = session.get(login_url)
result = session.post(login_url, data = values, headers = dict(referer=login_url))

# page = session.get(url)


#####




sauce = urllib.request.urlopen('https://intrahard.com/home/destacado/1').read()

soup = bs.BeautifulSoup(sauce, 'lxml')


print(soup)


