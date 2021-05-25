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


r = requests.get('http://naadyogacouncil.com')
start = timeit.default_timer()
soup = BeautifulSoup(r.text, 'html.parser')
links = []
linkss = []
dub_link = []
results = soup.findAll("ul", {"class": "card-list"})
# print(results)

results_li = soup.find_all("div", {"class": "event-wrapper"})
results_ = soup.find_all("div", {"class": "services-inside"})
# results_li ma 'card-genre' category che

# print(results_li)
# print(results_)

for i in results_li[:10]:
    for j in i.find_all('a'):
        links.append(j.get('href'))

for k in results_[:10]:
    for l in k.find_all('a'):
        linkss.append(l.get('href'))

# str1 = 'http://naadyogacouncil.com'
# all_links = prepend(links, str1)
# all_linkss = prepend(linkss, str1)

join_lists = links + linkss
for i in join_lists:
    if i not in dub_link:
        dub_link.append(i)

print(dub_link)

# right now 0.453 seconds ahiya suthi

for i in dub_link:
    o = requests.get(i)
    soup1 = BeautifulSoup(o.text, 'html.parser')
    # print(soup1)
    s = soup1.find('script', type="application/ld+json")
    # print(s)

    # i will check if Structured data is available or not.
    if s:
        print('------------------------------- S-DATA -----------------------------------------------------')

        Non_interesting_url = soup1.select('a[href]:not([href^="/"])')
        print(Non_interesting_url)
        # Non_interesting_url_a = Non_interesting_url.find_all('href')
        # print(Non_interesting_url_a)
        #
        # variable = soup1.select('a[href]:is([href^="https"])')
        # print(variable)

        json_object = json.loads(s.contents[0])
        print(json_object)
        if json_object is None:
            print('NonType')
            pass

        # print(json_object)
        cat_lists = ['Comedy', 'COVID-19', 'Workshop', 'Guitar', 'Online Tambola Housie', 'Online Ludo Saga',
                     'Screenwriting', 'Engineering', 'Computer Engineering', 'Civil Engineering', 'Sports']
        # word_tokens = word_tokenize(json_object['name'])
        # print(word_tokens)
        # filtered_sentences = [w for w in word_tokens if w in cat_lists]
        # print(filtered_sentences)
        # print('eventAttendanceMode :', json_object['eventAttendanceMode'])
        # print('name :', json_object['name'])
        # print('url :', json_object['url'])
        # print('startDate :', json_object['startDate'])
        # print('endDate :', json_object['endDate'])
        # print('description :', json_object['description'])
        # print('image :', json_object['image'])
        # print('performer-name :', json_object['performer']['name'])

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
        print('---------------------------- UData ----------------------------------------')
        print('url is: ', i)
        title4 = soup1.find('title')
        title44 = title4.string
        print(title44)
        eventMode4 = soup1.findAll("p", {"class": "css-1oqavfg"})

        desc4 = soup1.findAll("div", {"class": "unextended"})
        # desc44 = desc4.get('p')

        cat4 = soup1.findAll("p", {"class": "css-hc3kyf"})

        qr4 = soup1.findAll("img", {"class": "alignnone"})
        # qr44 = qr4.get('src')
        # print(qr44)
        # uData.objects.create(eventAttendanceMode=eventMode4,
        #                      name=title44,
        #                      description=desc4,
        #                      image=qr444,
        #                      category=cat4,
        #                      )
        print('website have not structured data')

stop = timeit.default_timer()
print('Time: ', stop - start)
