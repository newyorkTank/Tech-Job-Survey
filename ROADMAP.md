# Tech-Survey-Tool Roadmap

Tech-Survey-Tool v3 aims to scrap a popular online classified app for job listings and analyze which technologies are in demand by employers.

This roadmap represents some of priorities over the next couple months. Issues or pull requests will be opened to discuss each of these items as they progress.

## Front End Work
1. Setup a dataentry page in React
    - [ ] Create a React page
    - [ ] Create interface Pulldown of search_word lists, check box of categories
    - [ ] Create a Frame with checkboxes for markets including button for None, and All.
    - [ ] Create a React page
    - [ ] Create Button to Start
    - [ ] Create ticker box that is populated with same output that currently goes to the console.
1. Query database of results for a type of scrap over a restricted time period
1. Make a graph of results

## Analysis Work

Need to feed the correct batches of terms to count as ads go scraping by. Have to ignore terms within terms, and obvious redundancies. Also need to capture some chunk of text before and after for further analysis.

1. Store results in mySQL
1. Store results in mySQL
1. Make a React front end for data entry and displaying results
1. place on web-site
1. purge tags from description
1. make output for list_dict_4swords pretty
1. Installation (could it be made executable?)
1. Deal with variations of words (SQL, MSSQL, MySQL, NoSQL, Maria = SQL)
1. Deal with plurals, will make an exception from 4.
1. need to create exclusions i.e. ember but not member, java but not javascript
1. Decide what to keep from ads, and output that to a file
1. Create a loop at the bottom that offers user to print detail of one term.
1. Refactor, look for cleanups.
1. Create mechanism for picking one ad that contains several terms
1. Capture essential information for that ad
1. Send email with Custom Resume and cover letter to that company.
#### Completed
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

## Refactor

As the project evolves there is a tendency to get things done in lue of best programming practices. The aim here is to clean up the code.

- Replace Beautiful Soup with Scrapy
- Find redundancies and move them to functions
- Bundle functions into a module
