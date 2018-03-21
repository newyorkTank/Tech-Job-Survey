#####################
# parse4leftovers pulls out the best technology words from Craigslist to feed a new good words list.
# The reason to go through this process is because technology is shifting over time and by region.
# I just cut & paste a bunch of ads from diff cities, but same section i.e. internet_engineering.
# parse4leftovers takes a list of badwords, which is mostly 1000 common English words, and
# after running it a few times over a few hundred Craigslist ads to create
# another approximately 300 bad words added to the bad list. At last you  run to
# make a sorted list of high frequency technology words in a dictionary: good_words_*
#####################

from collections import Counter
def inList(word, list):
    if word in list:
        return True
    else:
        return False

# Grab the list of words to exclude
# These are single column in line
bwords = []
bw = open('bad_words', 'r', encoding='utf-8', errors='ignore')
lines = bw.readlines()
bw.close()
for line in lines:  # Clean off newline
    line = ''.join(filter(str.isalpha, line.lower().strip()))
    bwords.append(line)
# Grab the list of words from craigslist to parse
# This is sloppy text right out of Craigslist
filename = 'systems_network'
f = open(filename, 'r', encoding='utf-8', errors='ignore')
lines = f.readlines()
f.close()
# for x in range(0, 500): # Printing a sample for dev purpose
#     #print(lines[x])
#     texts.append(lines[x])
texts = []
gwords = []
for text in lines:
    words = text.split()  # Use first line to test parsing
    for word in words:
        word = ''.join(filter(str.isalpha, word.lower().strip()))
        if len(word) > 1:  # Purging empty words
            if not inList(word,bwords):  # Purging common words from bad_words file
                gwords.append(word)
sortedWords = Counter(gwords)
s = [(k, sortedWords[k]) for k in sorted(sortedWords, key=sortedWords.get, reverse=True)]
for k,v in s:
    if v > 2:
        print(k)
