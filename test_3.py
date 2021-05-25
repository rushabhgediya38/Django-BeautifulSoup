from bs4 import BeautifulSoup
import requests
import timeit
import json
from nltk.tokenize import word_tokenize
import re

# https://insider.in/all-for-one-a-fundraiser-for-covid-19-india-relief-may30-2021/event

r = requests.get('https://insider.in/learn-to-connect-with-your-inner-tutor-may30-2021/event')

soup = BeautifulSoup(r.text, 'html.parser')

# print(soup)

title = soup.find('title')
# print('title :', title.string)

# title = soup.find('title')
# print('title :', title.string)

teams = soup.findAll('img')
# print(teams)

sImg = []

for i in teams:
    src = i.get('src')
    sImg.append(src)
# print('Image :', sImg[0])


desc = ""
table = soup.findAll('section', {"class": "css-1rzyjn1"})
# print(table)
for i in table:
    for j in i.find_all('p'):
        desc += j.text

# print('desc :', desc)

cat = soup.findAll('div', {"class": "css-1jwr5f2"})
# print(cat)
cD = ""
for i in cat:
    for j in i:
        for k in j.find_all('p'):
            cD += k.text
print('category :', cD)

eventMode = []
eventMode4 = soup.findAll("p", {"class": "css-cd7xhm-Ee"})
# print(eventMode4)
for i in eventMode4:
    for k in i:
        eventMode.append(k)
print('eventName :', eventMode[0])
