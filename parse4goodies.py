#Imports
from collections import Counter
from bs4 import BeautifulSoup as bs4
import pandas as pd
import requests

# function inList
def inList(word, list):
    if word in list:
        return True
    else:
        return False

#########################################Begin
################ var declarations
cities = ['portland']
job_cats = {'eng':'internet-engineering'}
#cities = ['losangeles','seattle','newyork','chicago','dallas',
#          'houston','miami','atlanta','boston','washingtondc','philadelphia']
# More big Cities ,'sfbay' ,'denver' ,'phoenix'  ,'riverside'  ,'detroit'
# ,'seattle'  ,'minneapolis'  ,'sandiego'  ,'tampa'  ,'stlouis'
# Nice Cities  ,'portland'  ,'austin'  ,'colorado springs'  ,'boise'

#job_cats = {'eng':'internet-engineering','sof':'software-qa-dba-etc',
#            'tch':'technical-support','sad':'systems-networking'}
depth = 20  #Number of job ads per city
min = 1  #Threshold for caring
gwords = []
gwords_file = 'search_words'
list_results = []
list4counts = []

# Grab the list of good tech words to search for
# These are a single column text file
gw = open(gwords_file, 'r', encoding='utf-8', errors='ignore')
glines = gw.readlines()
gw.close()
for line in glines:  # Clean off newline
    line = line.strip()
    gwords.append(line.lower())

# Now begin crawling pages
for slum in cities:
    for cat in job_cats:
        url = 'https://' + slum + '.craigslist.org/' + cat
        rsp_page = requests.get(url, params='')
        search_html = bs4(rsp_page.text, 'html.parser')
        jobs = search_html.find_all('p', attrs={'class': 'result-info'})
        deep = depth if depth <= len(jobs) else len(jobs)
        for x in range(0, deep):
            search_element = jobs[x]
            dater = search_element.findAll(attrs={'class': 'result-date'})[0].text
            title = search_element.findAll(attrs={'class': 'result-title hdrlnk'})[0].text
            link = search_element.parent.contents[1].attrs['href']
            rsp_sub = requests.get(link, params='')
            job_html = bs4(rsp_sub.text, 'html.parser')
            job = job_html.find_all('section', attrs={'id': 'postingbody'})
            d = job[0].text
            # would like to pull email from here, also location
            d = d.lower()
            for p in gwords:
                if inList(p, d):
                    dict_results = {}
                    list4counts.append(p)
                    dict_results['term'] = p
                    dict_results['city'] = slum
                    dict_results['category'] = cat
                    dict_results['date'] = dater
                    dict_results['title'] = title
                    dict_results['link'] = link
                    dict_results['snippet'] = d[(d.index(p) - 30):(d.index(p) + 20)]
                    list_results.append(dict_results)

#Show all entries for one search word
s_word = 'ember'
#print(next((item for item in list_results if item['term'] == s_word)))
list_dict_4sword = [i for i in list_results if i['term'] == s_word]
for v in zip(list_dict_4sword):
    print(v)
# Sort and print quantities of found words
sortedWords = Counter(list4counts)
s = [(k, sortedWords[k]) for k in sorted(sortedWords, key=sortedWords.get, reverse=True)]
for k,v in s:
    if v > min - 1:
        print(str(v) + ', ' + k)


