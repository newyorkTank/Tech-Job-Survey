from collections import Counter
from bs4 import BeautifulSoup as bs4
import pandas as pd
import requests

url_base = 'https://losangeles.craigslist.org/search/sad'
#params = dict(bedrooms=1, is_furnished=1)
rsp = requests.get(url_base, params='')

print(rsp.url)

html = bs4(rsp.text, 'html.parser')
#print(html.prettify()[:20000])

jobs = html.find_all('p', attrs={'class': 'result-info'})
print(len(jobs))
this_job = jobs[15]
#print(this_job.prettify())
dater = this_job.findAll(attrs={'class': 'result-date'})[0].text
meta = this_job.findAll(attrs={'class': 'result-title hdrlnk'})[0].text
link = this_job.parent.contents[1].attrs['href']
#title = this_job.findAll(attrs={'class': 'result-meta'})[0].text
#tags = this_job.findAll(attrs={'class': 'result-tags'})[0].text
print('dater: ' + dater)
print('meta: ' + meta)
print('link: ' + link)
#print('title: ' + title)
#print('tags: ' + tags)
#print(this_job.prettify())

rsp2 = requests.get(link, params='')
print(rsp2.url)
html2 = bs4(rsp2.text, 'html.parser')
print(html2.prettify()[:20000])
jobs2 = html2.find_all('section', attrs={'id': 'postingbody'})
print(len(jobs2))
fred = jobs2[0].text
print(fred)
