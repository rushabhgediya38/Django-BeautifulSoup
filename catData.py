from bs4 import BeautifulSoup
import requests
import timeit
import json
from nltk.tokenize import word_tokenize
import re

# 1 https://www.naadyogacouncil.com/klangtherapie/was-ist-klangtherapie/  done
# 2 https://www.naadyogacouncil.com/naad-yoga/was-ist-naad-yoga/  done
# 3 https://www.naadyogacouncil.com/angebot/kursreihen/

r = requests.get('https://www.naadyogacouncil.com/angebot/kursreihen/')
start = timeit.default_timer()
soup = BeautifulSoup(r.text, 'html.parser')

# current_page_item
cat = []
results = soup.findAll("li", {"class": "current_page_item"})
for i in results:
    for j in i.find_all('a'):
        cat.append(j.text)
print(cat[0])