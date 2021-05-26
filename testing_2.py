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


r = requests.get('https://naadyogacouncil.com')
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

# print(dub_link)

# right now 0.453 seconds ahiya suthi

for i in dub_link:
    o = requests.get(i)
    soup1 = BeautifulSoup(o.text, 'html.parser')
    # print(soup1)
    s = soup1.find('script', type="application/ld+json")
    # print(s)

    # i will check if Structured data is available or not.
    if s:
        print('------------------------------------------ S-DATA -----------------------------------------------------')

        Non_interesting_url = soup1.select('a[href]:not([href^="/"])')
        for link in Non_interesting_url:
            if link.get('href') != '#':
                print(link)

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
        # cat_lists = ['Comedy', 'COVID-19', 'Workshop', 'Guitar', 'Online Tambola Housie', 'Online Ludo Saga',
        #              'Screenwriting', 'Engineering', 'Computer Engineering', 'Civil Engineering', 'Sports']
        #
        # word_tokens = word_tokenize(json_object[0]['name'])
        # print(word_tokens)
        # filtered_sentences = [w for w in word_tokens if w in cat_lists]
        # print(filtered_sentences)
        # print('eventAttendanceMode :', json_object['eventAttendanceMode'])
        # print('name :', json_object['description'])
        print('url :', json_object[0]['url'])

        print('description :', json_object[0]['description'])
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

        title = soup.find('title')
        print('title :', title.string)

        teams = soup.findAll('img', {'class': 'size-full'})
        # print(teams)

        sImg = []

        for i in teams:
            src = i.get('src')
            sImg.append(src)

        print('Image :', sImg[0])

        desc = []
        table = soup.find_all('div', {"class": "unextended"})
        # print(table)
        for i in table:
            for j in i.find_all('p'):
                desc.append(j.text)

        # print('desc :', desc)
        eventMode = ""
        eventMode4 = soup.find_all("h2", {"class": "text-divider-double"})
        for i in eventMode4:
            eventMode += i.text

        print('eventName :', eventMode)

stop = timeit.default_timer()
print('Time: ', stop - start)
