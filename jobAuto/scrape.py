import requests
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import json
import re
import urllib.parse
# getting user I/O
with open('user.json') as details:
    user_data = json.load(details)
# Create the URL
for key in user_data['Role']:
    role=key
    break
url='{"roles"'+':["'+str(role)+'","'+str(user_data['Role'][role][0])+'"]}'
user_url=urllib.parse.quote(url, safe='~@#$&()*!+=:;,.?/\'')


session = requests.session()
r = session.get('https://angel.co/login')
soup = BeautifulSoup(r.text,features="html.parser")
authenticity_token = soup.findAll("input", {"name":"authenticity_token"})[0].get('value')
payload = {'user[email]':'mrahul.krishnan@gmail.com','user[password]':'manamongmen','authenticity_token':authenticity_token,'login_only':'true'}

r = session.post('https://angel.co/login',payload)
r = session.get('https://angel.co/jobs#find/f!'+user_url)

soup =BeautifulSoup(r.text, features="html.parser")


