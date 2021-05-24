from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import json
from collections import Counter


def prepend(list, str):
    # Using format()
    str += '{0}'
    list = [str.format(i) for i in list]
    return (list)


def home(request):
    if request.method == 'POST':
        url = request.POST['freq_url']

        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        links = []
        # print(type(links))
        for ultag in soup.find_all('ul', {'class': 'card-list'}):
            for litag in ultag.find_all('li', {'class': 'card-list-item'})[:10]:

                for all_tag in litag.find_all('a'):
                    # print(type(all_tag))
                    links.append(all_tag.get('href'))
        str1 = 'https://insider.in'
        all_links = prepend(links, str1)
        print(all_links)
        kk = all_links
        # a = links[1]
        # # print(type(a))
        # b = links[2]
        # c = links[3]
        # d = links[4]
        # e = links[5]
        # f = links[6]
        # g = links[7]
        # h = links[8]
        # i = links[9]
        # all_data_link = [a, b, c, d, e, f, g, h, i]
        return render(request, 'Home.html', {'add': kk})
        # parent = soup.find("body").find("ul")
        # text = list(parent.descendants)

        # s = soup.find('script', type="application/ld+json")
        # json_object = json.loads(s.contents[0])
        # print(json_object['eventAttendanceMode'])
        # print(json_object['name'])
        # print(json_object['url'])
        # print(json_object['startDate'])
        # print(json_object['endDate'])
        # # print(json_object['description'])
        # print(json_object['image'])
        # urls = [el['url'] for el in json.loads(s.text)['itemListElement']]

    if request.method == 'GET':
        return render(request, 'Home.html')
