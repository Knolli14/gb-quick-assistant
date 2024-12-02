import requests
from bs4 import BeautifulSoup

from gb_assistant.params import RAW_DATA_PATH, SEARCH_PAGE_URL

class PDFHandler:
    ''' Class handling Extraction from web '''

    URL = SEARCH_PAGE_URL

    def __init__(self):
        pass



    def extract_games_list(self):
        pass

        # loop over all pages

            # get soup of a page
            # find all games tags



    def _get_soup(self, page=1):
        ''' Creates a SoupObject from the Search Page using html.parser '''

        # create connection to url
        response = requests.get(self.URL + str(page))

        return BeautifulSoup(response.content, "html.parser")

    def _get_all_tags(self, language="English"):
        ''' Extracts all games of a html soup'''

        soup = self._get_soup()

        games = soup.find_all(
            class_="btn btn-sm btn-secondary mb-1",
            title="In "+language
        )

        return games

if __name__ == "__main__":

    handler = PDFHandler()
    soup = handler._get_soup()

    print(type(soup), 30*"-", sep="\n")
    print(soup)
