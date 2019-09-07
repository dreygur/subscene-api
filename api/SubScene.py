import sys
import time
from requests import get, post
from bs4 import BeautifulSoup

class SubScene:
    # Subscene api
    def __init__(self):
        self.name = __name__
        self.link = 'https://subscene.com'

    def getDetail(self, detail):
        # Search for a specific movie
        # and scrape intended one from the list
        try:
            data = {
                'query': detail['name']
            }
            while True:
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
            links = []

            try:
                if h2[0]['class'][0].title() == 'Exact':
                    if len(ul[0].findAll('a')) > 1:
                        for a in ul[0].findAll('a'):
                            links.append(self.link+a.get('href'))
                            if detail.get('year') != '' and detail.get('year') in a.text:
                                return links[-1]
                        else:
                            return self.getFromFullChoice(h2, ul, detail)
                    else:
                        if detail.get('year') != '' and detail.get('year') in ul[0].find('a').text:
                            return self.link + ul[0].find('a')['href']
                        else:
                            return self.getFromFullChoice(h2, ul, detail)
                else:
                    return self.getFromFullChoice(h2, ul, detail)
            except Exception as e:
                print(e)
                return None
        except Exception as e:
            print(e)
            return None