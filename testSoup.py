import bs4 as bs
import urllib.request

# source = urllib.request.urlopen('https://www.nytimes.com/2020/06/23/world/europe/coronavirus-EU-American-travel-ban.html?action=click&module=Top%20Stories&pgtype=Homepage').read()

source = urllib.request.urlopen('https://www.nytimes.com').read()

soup = bs.BeautifulSoup(source,'lxml')

# searching for paragraphs in general
# for paragraph in soup.find_all('p'):
#     print(paragraph.text)

# searching for reddit headlines
# for headline in soup.find_all('h3'):
#     print(headline.text)

# searching for nytimes headlines
for heading in soup.find_all('h2'):
    print(heading.text)

# allow people to look at this, and to input their own links. 

# print(soup)

# print(soup.title)
# print(soup.p)
# print(soup.find_all('p'))

# print(soup.get_text())

# for url in soup.find_all('a'):
#     print(url.get('href'))

