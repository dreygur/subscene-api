import sys
import time
from requests import get, post
from bs4 import BeautifulSoup

# Prohbit system from writing byte-codes
sys.dont_write_bytecode = True

class SubScene:
    # Subscene api

    def __init__(self):
        self.name = __name__
        self.link = 'https://subscene.com'
        self.lang = 'English'

    def getDetail(self, detail):
        # Search for a specific movie
        # and scrape intended one from the list

        try:
            data = {
                # We have got detail as a list
                'query': detail['name']
            }
            
            while True:
                # Loop till we don't get any answer from server
                search = post(self.link + '/subtitles/searchbytitle', data=data)
                # print(search.status_code)
                if search.status_code != 200:
                    time.sleep(3)
                else:
                    break

            soup = BeautifulSoup(search.text, 'html.parser')
            div = soup.find('div', {'class': 'search-result'})
            h2 = div.findAll('h2')
            ul = div.findAll('ul')
            links = [] # All the links will be stored here

            try:
                if h2[0]['class'][0].title() == 'Exact': # Use the links under 'Exact' heading
                    if len(ul[0].findAll('a')) > 1:
                        for a in ul[0].findAll('a'):
                            links.append(self.link+a.get('href'))
                            if detail['year'] != '' and detail['year'] in a.text:
                                return links[0]
                        
            except Exception as e:
                # print(e)
                return None

        except Exception as e:
            # print(e)
            return None

    def getSubLink(self, link):
        # Get Direct Link for Downloading Subtitle
        # Link is the Search Results page link

        html = get(link).text
        soup = BeautifulSoup(html, 'html.parser')
        languages = soup.find('tbody').findAll('a')
        langs, subs, links = [], [], []

        for i in languages:
            al = i.findAll('span')
            try:
                la = al[0].text.strip()
                if la == self.lang or la == 'English':
                    langs.append(la)
                    subs.append(al[1].text.strip())
                    links.append(self.link + i['href'])
            except Exception:
                pass
        
        for l, s, li in zip(langs, subs, links):
                if l == self.lang: # and 'positive-icon' in a.span['class']
                    # print(f'Subtitle name: {s}\nLink: {links}')
                    return links
        # return None
    

    def getDownLink(self, link):
        # Gets the Direct Download Link from SubScene

        html = get(link).text
        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find('div', {'class': 'download'})
        return self.link + div.a['href']

# sub = SubScene() # Initialize the api Class
# detail = {
#     'name': 'Hello',
#     'year': '2008'
# }
# link = sub.getDetail(detail)
# links = sub.getSubLink(link)
# down = sub.getDownLink(links[0])
# print(down)