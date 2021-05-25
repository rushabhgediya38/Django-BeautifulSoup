from django.shortcuts import render, HttpResponse
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
import requests
import timeit
import json
from sApp.models import sData, InterestingUrl, Non_interesting_url

# https://insider.in/all-fundraising-week-events-in-online?utm_source=Insider&utm_medium=CityBanner


def prepend(list, str):
    # Using format()
    str += '{0}'
    list = [str.format(i) for i in list]
    return (list)


def home(request):
    if request.method == 'POST':
        url = request.POST['freq_url']
        # testing_data()
        # print(url)
        # ['1', '2']
        r = requests.get(url)
        start = timeit.default_timer()
        soup = BeautifulSoup(r.text, 'html.parser')
        links = []
        # results = soup.findAll("ul", {"class": "card-list"})
        # print(results)
        results_li = soup.findAll("li", {"class": "card-list-item"})
        # print(results_li)

        for i in results_li[:10]:
            for j in i.find_all('a'):
                links.append(j.get('href'))

        str1 = url
        all_links = prepend(links, str1)
        # print(all_links)

        # right now 0.453 seconds

        for i in all_links[:10]:
            o = requests.get(i)
            soup1 = BeautifulSoup(o.text, 'html.parser')
            # print(soup1)
            s = soup1.find('script', type="application/ld+json")
            # print(s)
            if s:
                Non_interesting_urls = soup1.select('a[href]:not([href^="/"])')

                for i in Non_interesting_urls:
                    nonUrl = i.get('href')
                    Non_interesting_url.objects.create(Non_interesting_url1=nonUrl)
                    print('run Non_interesting_url')

                json_object = json.loads(s.contents[0])

                if json_object is None:
                    print('NonType')
                    pass

                cat_lists = ['Comedy', 'COVID-19', 'Workshop', 'Guitar', 'Online Tambola Housie', 'Online Ludo Saga',
                             'Screenwriting', 'Engineering', 'Computer Engineering', 'Civil Engineering', 'Sports',
                             'Spirituality', 'Cello', 'Python', 'Wines', 'Computer Engineering', 'Cvil',
                             'Civil Engineering', 'Ludo', 'Cosmetics', 'Workshop', 'Stock Market', 'Sales']
                word_tokens = word_tokenize(json_object['name'])
                # print(word_tokens)
                filtered_sentences = [w for w in word_tokens if w in cat_lists]

                # print(filtered_sentences)
                print('eventAttendanceMode :', json_object['eventAttendanceMode'])
                print('name :', json_object['name'])
                # print('url :', json_object['url'])
                # print('startDate :', json_object['startDate'])
                # print('endDate :', json_object['endDate'])
                # print('description :', json_object['description'])
                # print('image :', json_object['image'])
                # print('performer-name :', json_object['performer']['name'])
                # print('category :', filtered_sentences)
                print('------------------------------------------------------------------------------------')
                Interesting_url = json_object['url']
                print(Interesting_url)
                InterestingUrl.objects.create(Interesting_url1=json_object['url']),

                sData.objects.create(eventAttendanceMode=json_object['eventAttendanceMode'],
                                     name=json_object['name'],
                                     description=json_object['description'],
                                     image=json_object['image'],
                                     startDate=json_object['startDate'],
                                     endDate=json_object['endDate'],
                                     performer_name=json_object['performer']['name'],
                                     category=filtered_sentences,
                                     )

            else:
                print('website have not structured data')
        stop = timeit.default_timer()
        print('Time: ', stop - start)
        return HttpResponse('all data success')
        # 8 to 11 seconds for 10 items

    else:
        return render(request, 'Home.html')
