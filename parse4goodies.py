#####################
# 1. Reverse and search for good_words*
# 2. Deal with phrases (Active Directory, Amazon Web Services)
# 3. Deal with variations of words (SQL, MSSQL, MySQL, NoSQL, Mongo, Maria)
# 4. Deal with special characters C#, C++, stuff with dashes
# 5. Deal with plurals
# 5. Limit count per ad, by doing the parsing on a ad by ad basis
# 5. and by not counting terms that get repeated in the same ad
# 6. Implement inputs, and pretty up the output to a file
# 7. Scrap not cut-n-paste
# 8. Crawl the web
#####################
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

#Begin
# var declerations
source_file = 'internet_engineering'
searchwords_file = 'good_words'
url_base = 'http://sfbay.craigslist.org/search/eby/apa'
params = dict(bedrooms=1, is_furnished=1)
rsp = requests.get(url_base, params=params)

# Grab the list of words to search for
# These are a single column text file
gwords = []
gw = open(searchwords_file, 'r', encoding='utf-8', errors='ignore')
glines = gw.readlines()
gw.close()
for line in glines:  # Clean off newline
    line = line.strip()
    gwords.append(line.lower())
# Grab the list of words from craigslist to parse
# This is sloppy text right out of Craigslist
ad_texts = []
ad_file = open(source_file, 'r', encoding='utf-8', errors='ignore')
ad_texts = ad_file.read().split('&&&')
ad_file.close()
# Check if ad contains tech words from list and append to new list
l = []
for ad in ad_texts:
    ad = ad.lower()
    for p in gwords:
        if inList(p,ad):
            l.append(p)
# Sort and print quantities of found words
sortedWords = Counter(l)
s = [(k, sortedWords[k]) for k in sorted(sortedWords, key=sortedWords.get, reverse=True)]
for k,v in s:
    if v > 0:
        print(str(v) + ', ' + k)
