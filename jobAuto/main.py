import json
from selenium import webdriver
import urllib.parse


browser = webdriver.Firefox()
browser.get('https://angel.co/login')

#login
browser.find_element_by_xpath('//*[@id="user_email"]').send_keys('mrahul.krishnan@gmail.com')
browser.find_element_by_xpath('//*[@id="user_password"]').send_keys('manamongmen')

browser.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div/div/div/div[1]/div[1]/form/div[2]/input').click()

# executing the selection

with open('user.json') as details:
    user_data = json.load(details)
# Create the URL
for key in user_data['Role']:
    role=key
    break
url='{"roles"'+':["'+str(role)+'","'+str(user_data['Role'][role][0])+'"]}'
user_url=urllib.parse.quote(url, safe='~@#$&()*!+=:;,.?/\'')
browser.get('https://angel.co/jobs#find/f!'+user_url)














