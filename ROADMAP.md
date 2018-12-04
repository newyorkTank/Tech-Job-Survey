# Tech-Survey-Tool Roadmap

Tech-Survey-Tool v3 aims to scrap Craigslist for job listings and analyze which technologies are in demand by employers.

This roadmap represents some of priorities over the next couple months. Issues or pull requests will be opened to discuss each of these items as they progress.

## 1. Front End Work

1. - [ ] Setup a dataentry page in React
1. - [ ] Kick off a scrap
1. - [ ] Display results in a frame on the original page
1. - [ ] Query database of results for a type of scrap over a restricted time period
1. - [ ] Make a graph of results

## 2. Analysis Work

Need to feed the correct batches of terms to count as ads go scrapying by. Have to ignore terms within terms, and obvious redundancies. Also need to capture some chunk of text before and after for further analysis.

- [ ] Store results in mySQL
- [ ] Store results in mySQL
- [ ] Make a React front end for data entry and displaying results
- [ ] place on web-site
- [ ] purge tags from description
- [ ] make output for list_dict_4swords pretty
- [ ] Installation (could it be made executable?)
- [ ] Deal with variations of words (SQL, MSSQL, MySQL, NoSQL, Maria = SQL)
- [ ] Deal with plurals, will make an exception from 4.
- [ ] need to create exclusions i.e. ember but not member, java but not javascript
- [ ] Decide what to keep from ads, and output that to a file
- [ ] Create a loop at the bottom that offers user to print detail of one term.
- [ ] Refactor, look for cleanups.
- [ ] Create mechanism for picking one ad that contains several terms
- [ ] Capture essential information for that ad
- [ ] Send email with Custom Resume and cover letter to that company.
- [x] Limit count per ad, by doing the parsing on an ad by ad basis
- [x] and by not counting terms that get repeated in the same ad
- [x] Scrap not cut-n-paste
- [x] Make parse4leftovers.py use scrapping, and add more words to search_word
- [x] Crawl the web
- [x] Capture chunk 25 chars before and after.
- [x] Ticker - spinney wheel and dots across the screen(like dot/5 ads)
- [x] Have dedup offer to replace search_words with deduped sorted list
- [x] Deal with phrases (Active Directory, Amazon Web Services)
- [x] Deal with special characters C#, C++, stuff with dashes
- [x] Reverse and search for good_words*

## 3. Refactor

As the project evolves there is a tendency to get things done in lue of best programming practices. The aim here is to clean up the code.

- Replace Beautiful Soup with Scrapy
- Find redundancies and move them to functions
- Bundle functions into a module
