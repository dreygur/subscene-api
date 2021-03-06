import sys
import time
import requests
from bs4 import BeautifulSoup

# Prohibit system from writing byte-codes
sys.dont_write_bytecode = True

class SubScene:
    """
    SubScene api
    Methods:
        * getDetail()
            Gets Detailed Information and Link to the subtitle
        * getSubLink()
            Loads the Subtitle Link
        * getDownLink()
            Generate download link upon users language choice
    """

    def __init__(self):

        """
        Class Initialization
        Also some defaults values are set.
        You can change them if you want
        """
        self.name = __name__
        self.link = 'https://subscene.com'
        self.lang = 'English'

    def getDetail(self, detail):

        """
        Search's for a specific movie/media
        and scrape intended one from the list
        """

        try:
            data = {
                # We have got detail as a list
                'query': detail['name']
            }

            while True:
                # Loop till we don't get any answer from server
                search = requests.post(self.link + '/subtitles/searchbytitle', data=data)
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
                            links.append(self.link + a['href'])
                            if detail['year'] != '' and detail['year'] in a.text:
                                return links[0]

            except Exception as e:
                # print(e)
                return e

        except Exception as e:
            # print(e)
            return e

    def getSubLink(self, link, lang='English'):
        """
        Get Direct Link for Downloading Subtitle
        Link is the Search Results page link
        You can pass your desired Language

        Args:
            link: link of subtitle
            lang: desired language, default 'English'
        
        Returns:
            Returns a list of urls
        """

        try:
            html = requests.get(link).text
        except requests.exceptions.MissingSchema:
            return 'Subtitle not Found. Try Changing the Name or year or language or both'
        soup = BeautifulSoup(html, 'html.parser')
        languages = soup.find('tbody').findAll('a')
        langs, subs, links = [], [], []

        for language in languages:
            all_lang = language.findAll('span')
            try:
                lan = all_lang[0].text.strip()
                if lan == self.lang or lan == lang:
                    langs.append(lan)
                    subs.append(all_lang[1].text.strip())
                    links.append(self.link + language['href'])
            except Exception:
                pass

        return links

        # for l, s, li in zip(langs, subs, links):
        #     if l == self.lang: # and 'positive-icon' in a.span['class']
        #         # print(f'Subtitle name: {s}\nLink: {links}')
        #         return links
        # return None


    def getDownLink(self, link):

        """
        Gets the Direct Download Link from SubScene

        Args:
            link: link of subtitle
        
        Returns:
            the url as a string
        """

        try:
            html = requests.get(link).text
        except requests.exceptions.MissingSchema:
            return 'Subtitle not Found. Try Changing the Name or year or language or both'

        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find('div', {'class': 'download'})
        return self.link + div.a['href']
