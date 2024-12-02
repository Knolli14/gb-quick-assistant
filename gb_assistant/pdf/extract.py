import requests
from bs4 import BeautifulSoup

from params import RAW_DATA_PATH

class PDFExtractor:
    ''' Class handling Extraction from web '''

    URL = RAW_DATA_PATH

    def get_soup(self, page=1):
        ''' Creates a SoupObject from the Search Page using html.parser '''

        # create connection to url
        response = requests.get(__class__.URL)

        return BeautifulSoup(response.content, "html.parser")
