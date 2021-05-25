from django.shortcuts import render, HttpResponse, redirect
from bs4 import BeautifulSoup
import requests
import timeit
import json
from sApp.models import sData, InterestingUrl, Non_interesting_url, uData


# https://insider.in/all-fundraising-week-events-in-online?utm_source=Insider&utm_medium=CityBanner


def prepend(list, str):
    # Using format()
    str += '{0}'
    list = [str.format(i) for i in list]
    return (list)


def home(request):
    if request.method == 'POST':
        url = request.POST['freq_url']
        if url == "https://insider.in":
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
                    print(
                        '----------------------------SData-------------------------------------------------------------')
                    Non_interesting_urls = soup1.select('a[href]:not([href^="/"])')

                    for i in Non_interesting_urls:
                        nonUrl = i.get('href')
                        if nonUrl != '#':
                            if not nonUrl.startswith("tel"):
                                Non_interesting_url.objects.create(Non_interesting_url1=nonUrl)
                                print('run Non_interesting_url')

                    cat = soup1.findAll('div', {"class": "css-1jwr5f2"})
                    # print(cat)
                    cD = ""
                    for i in cat:
                        for j in i:
                            for k in j.find_all('p'):
                                cD += k.text
                    cat_get = cD

                    json_object = json.loads(s.contents[0])

                    if json_object is None:
                        print('NonType')
                        pass

                    # print(filtered_sentences)
                    # print('eventAttendanceMode :', json_object['eventAttendanceMode'])
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
                                         category=json_object['name'],
                                         )

                else:

                    print(
                        '----------------------------UData----------------------------------------------------------')
                    Non_interesting_urls = soup1.select('a[href]:not([href^="/"])')

                    for i in Non_interesting_urls:
                        nonUrl = i.get('href')
                        if nonUrl != '#':
                            if not nonUrl.startswith("tel"):
                                Non_interesting_url.objects.create(Non_interesting_url1=nonUrl)
                                print('Run UData - Non_interesting_url')

                    title = soup.find('title')
                    title_get = title.string

                    teams = soup.findAll('img')
                    sImg = []
                    for i in teams:
                        src = i.get('src')
                        sImg.append(src)
                    img_get = sImg[0]
                    # print('Image :', sImg[0])

                    desc = ""
                    table = soup.findAll('section', {"class": "css-1rzyjn1"})
                    # print(table)
                    for i in table:
                        for j in i.find_all('p'):
                            desc += j.text

                    desc_get = desc

                    cat = soup.findAll('div', {"class": "css-1jwr5f2"})
                    # print(cat)
                    cD = ""
                    for i in cat:
                        for j in i:
                            for k in j.find_all('p'):
                                cD += k.text
                    cat_get = cD

                    eventMode = []
                    eventMode4 = soup.findAll("p", {"class": "css-cd7xhm-Ee"})
                    print(eventMode4)
                    for i in eventMode4:
                        for k in i:
                            eventMode.append(k)
                    eventAMode = eventMode[0]

                    uData.objects.create(eventAttendanceMode=eventAMode,
                                         name=title_get,
                                         description=desc_get,
                                         image=img_get,
                                         category=cat_get,
                                         )

            stop = timeit.default_timer()
            print('Time: ', stop - start)
            return redirect('sData')
        elif url == "http://naadyogacouncil.com":
            r = requests.get(url)
            # start = timeit.default_timer()
            soup = BeautifulSoup(r.text, 'html.parser')
            links = []
            linkss = []
            dub_link = []

            results_li = soup.find_all("div", {"class": "event-wrapper"})
            results_ = soup.find_all("div", {"class": "services-inside"})

            for i in results_li[:10]:
                for j in i.find_all('a'):
                    links.append(j.get('href'))

            for k in results_[:10]:
                for l in k.find_all('a'):
                    linkss.append(l.get('href'))

            join_lists = links + linkss
            for i in join_lists:
                if i not in dub_link:
                    dub_link.append(i)

            for i in dub_link:
                o = requests.get(i)
                soup1 = BeautifulSoup(o.text, 'html.parser')
                # print(soup1)
                s = soup1.find('script', type="application/ld+json")
                # print(s)

                # i will check if Structured data is available or not.
                if s:
                    print(
                        '------------------------------------------ S-DATA '
                        '-----------------------------------------------------')

                    Non_interesting_urls = soup1.select('a[href]:not([href^="/"])')
                    for i in Non_interesting_urls[5:15]:
                        nonUrl = i.get('href')
                        if nonUrl != '#':
                            if not nonUrl.startswith("tel"):
                                Non_interesting_url.objects.create(Non_interesting_url1=nonUrl)
                                print('run Non_interesting_url')

                    # variable = soup1.select('a[href]:is([href^="https"])')
                    # print(variable)

                    json_object = json.loads(s.contents[0])
                    print(json_object)
                    if json_object is None:
                        print('NonType')
                        pass

                    try:
                        img2 = json_object[0]['image']
                    except KeyError as ke:
                        img2 = ""

                    try:
                        performer2 = json_object[0]['performer']
                    except KeyError as ke:
                        performer2 = ""

                    # print(sDate2)
                    # print(eDate2)
                    # print(img2)
                    # print(performer2)
                    InterestingUrl.objects.create(Interesting_url1=json_object[0]['url']),

                    sData.objects.create(
                        name=json_object[0]['name'],
                        description=json_object[0]['description'],
                        image=img2,
                        performer_name=performer2,
                        category=json_object[0]['@type'])

                    # 7 seconds for 10 items
                else:
                    print('---------------------------- UData ----------------------------------------')
                    print('url is: ', i)

                    Non_interesting_urls = soup1.select('a[href]:not([href^="/"])')
                    for i in Non_interesting_urls[5:15]:
                        nonUrl = i.get('href')
                        if nonUrl != '#':
                            if not nonUrl.startswith("tel"):
                                Non_interesting_url.objects.create(Non_interesting_url1=nonUrl)
                                print('run UData - Non_interesting_url')

                    title = soup.find('title')

                    cat = []
                    results = soup1.findAll("li", {"class": "current_page_item"})
                    for i in results:
                        for j in i.find_all('a'):
                            cat.append(j.text)

                    print('cat:', cat[0])

                    teams = soup1.findAll('img', {'class': 'size-full'})
                    sImg = []
                    if teams:
                        for i in teams:
                            src = i.get('src')
                            sImg.append(src)

                    if sImg:
                        single_img1 = sImg[0]
                    else:
                        single_img1 = False

                    single_img2 = single_img1

                    desc = ""
                    table = soup1.find_all('div', {"class": "unextended"})
                    # print(table)
                    for i in table:
                        for j in i.find_all('p'):
                            desc += j.text

                    # print('desc :', desc)

                    eventMode = ""
                    eventMode4 = soup1.find_all("h2", {"class": "text-divider-double"})
                    for i in eventMode4:
                        eventMode += i.text

                    # print('event', eventMode)

                    eventModeU = eventMode
                    titleU = title.string
                    descU = desc
                    sImgU = single_img2
                    catU = cat[0]

                    uData.objects.create(eventAttendanceMode=eventModeU,
                                         name=titleU,
                                         description=descU,
                                         image=sImgU,
                                         category=catU,
                                         )

            return redirect('sData')
        else:
            return HttpResponse('url does not support')
    else:
        return render(request, 'Home.html')


# Structured data.
def s_Data(request):
    asd = sData.objects.all()
    return render(request, 'all_structuredData.html', {'sData': asd})


# Un-Structured data.
def u_Data(request):
    ausd = uData.objects.all()
    return render(request, 'all_UnS_Data.html', {'UsData': ausd})


# InterestingUrl
def iUrl(request):
    aIURl = InterestingUrl.objects.all()
    return render(request, 'all_iUrl.html', {'iUrl': aIURl})


# Non_interesting_url
def nUrl(request):
    nIURl = Non_interesting_url.objects.all()
    return render(request, 'all_nUrl.html', {'nUrl': nIURl})
