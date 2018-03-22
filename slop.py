# from collections import Counter
# from bs4 import BeautifulSoup as bs4
# import pandas as pd
# import requests
#
# city = 'losangeles'
# job_cat = 'sad'
# depth = 5
# url = 'https://' + city + '.craigslist.org/search/' + job_cat
# #params = dict(bedrooms=1, is_furnished=1)
# rsp_page = requests.get(url, params='')
# #print(rsp.url)
# search_html = bs4(rsp_page.text, 'html.parser')
# #print(search_html.prettify()[:20000])
# jobs = search_html.find_all('p', attrs={'class': 'result-info'})
# #print(len(jobs))
# for x in range(0, depth):
#     search_element = jobs[x]
#     #print(this_job.prettify())
#     dater = search_element.findAll(attrs={'class': 'result-date'})[0].text
#     title = search_element.findAll(attrs={'class': 'result-title hdrlnk'})[0].text
#     link = search_element.parent.contents[1].attrs['href']
#     #print('dater: ' + dater)
#     #print('meta: ' + meta)
#     #print('link: ' + link)
#     #print(a_job.prettify())
#     rsp_sub = requests.get(link, params='')
#     #print(rsp_sub.url)
#     job_html = bs4(rsp_sub.text, 'html.parser')
#     #print(job_html.prettify()[:20000])
#     job = job_html.find_all('section', attrs={'id': 'postingbody'})
#     #print(len(job))
#     description = job[0].text
#     print(title)
#     print(description[30:80] + '. . . ')
#     print('===============================================')
#
# ad_texts = []
# ad_file = open(source_file, 'r', encoding='utf-8', errors='ignore')
# ad_texts = ad_file.read().split('&&&')
# ad_file.close()
# # Check if ad contains tech words from list and append to new list
# l = []
# for ad in ad_texts:

job_cats = {'eng':'internet-engineering','sof':'software-qa-dba-etc',
            'tch':'technical-support','sad':'systems-networking'}

for cat in job_cats:
    print(cat)
depth = 5
min = 3
dep = 0
fred = 'False'
dep = depth if depth > min else min
print(dep)
fruit = 'Apple'
isApple = True if fruit == 'Apple' else False
print(isApple)

s1 = "this is the first line.\nthis is bbbb the second line\nthe third stops abrubptly "
s2 = "bbbb"

print(s1[(s1.index(s2) - 20):(s1.index(s2)+20)])