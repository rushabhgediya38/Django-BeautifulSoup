from bs4 import BeautifulSoup
import requests
import timeit
import json
from nltk.tokenize import word_tokenize
import re


def prepend(list, str):
    # Using format()
    str += '{0}'
    list = [str.format(i) for i in list]
    return (list)


r = requests.get('https://insider.in')
start = timeit.default_timer()
soup = BeautifulSoup(r.text, 'html.parser')
links = []
# results = soup.findAll("ul", {"class": "card-list"})
# print(results)
results_li = soup.findAll("li", {"class": "card-list-item"})
#  results_li ma 'card-genre' category che
# print(results_li)


# non interesting url
# for link1 in soup.select('a[href]:not([href^="/"])'):
#     print(link1)


# one by one link pass thase

for i in results_li[:10]:
    for j in i.find_all('a'):
        links.append(j.get('href'))

str1 = 'https://insider.in'
all_links = prepend(links, str1)

# print(all_links)

# right now 0.453 seconds ahiya suthi

for i in all_links:
    o = requests.get(i)
    soup1 = BeautifulSoup(o.text, 'html.parser')
    # print(soup1)
    s = soup1.find('script', type="application/ld+json")
    # print(s)

    # i will check if Structured data is available or not.
    if s:
        Non_interesting_url = soup1.select('a[href]:not([href^="/"])')
        for i in Non_interesting_url:
            link = i.get('href')
            print(link)
        print(Non_interesting_url)
        Non_interesting_url_a = Non_interesting_url.find_all('href')
        print(Non_interesting_url_a)

        variable = soup1.select('a[href]:is([href^="https"])')
        print(variable)

        json_object = json.loads(s.contents[0])
        if json_object is None:
            print('NonType')
            pass

        # print(json_object)
        cat_lists = ['Comedy', 'COVID-19', 'Workshop', 'Guitar', 'Online Tambola Housie', 'Online Ludo Saga',
                     'Screenwriting', 'Engineering', 'Computer Engineering', 'Civil Engineering', 'Sports']
        word_tokens = word_tokenize(json_object['name'])
        # print(word_tokens)
        filtered_sentences = [w for w in word_tokens if w in cat_lists]
        # print(filtered_sentences)
        print('eventAttendanceMode :', json_object['eventAttendanceMode'])
        print('name :', json_object['name'])
        print('url :', json_object['url'])
        # print('startDate :', json_object['startDate'])
        # print('endDate :', json_object['endDate'])
        # print('description :', json_object['description'])
        # print('image :', json_object['image'])
        # print('performer-name :', json_object['performer']['name'])
        print('------------------------------------------------------------------------------------')

        # sData.objects.create(eventAttendanceMode=json_object['eventAttendanceMode'],
        #                      name=json_object['name'],
        #                      description=json_object['description'],
        #                      url=json_object['url'],
        #                      image=json_object['image'],
        #                      startDate=json_object['startDate'],
        #                      endDate=json_object['endDate'],
        #                      performer_name=json_object['performer']['name'])

        # 7 seconds for 10 items
    else:
        title4 = soup1.find('title')
        title44 = title4.string
        print(title44)
        eventMode4 = soup1.findAll("p", {"class": "css-1oqavfg"})
        desc4 = soup1.findAll("section", {"class": "css-1rzyjn1"})
        cat4 = soup1.findAll("p", {"class": "css-hc3kyf"})

        qr4 = soup1.findAll("div", {"class": "css-79elbk"})
        qr44 = qr4.findAll("img")
        qr444 = qr44.get('src')
        print(qr444)
        # uData.objects.create(eventAttendanceMode=eventMode4,
        #                      name=title44,
        #                      description=desc4,
        #                      image=qr444,
        #                      category=cat4,
        #                      )
        print('website have not structured data')
    #
    # stop = timeit.default_timer()
    # print('Time: ', stop - start)
