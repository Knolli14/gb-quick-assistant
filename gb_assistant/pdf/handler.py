import requests
from bs4 import BeautifulSoup

from gb_assistant.params import *

class PDFHandler:
    ''' Class handling Extraction from web '''

    URL = SEARCH_PAGE_URL

    def __init__(self, games_list=None):
        self.games_list = games_list if games_list else []


    def extract_games_list(self, language="English") -> list:
        ''' Ectract a List of dicts with url and title of Boardgames '''

        # helper function to extract title
        def _extract_title(url) -> str:
            ''' Extract title out of link'''

            title_full = url.split("/")[-1] \
                            .strip(".pdf")

            return " ".join(title_full.split("-")[1:-1])

        # helper function to get soup and extract tags
        def _extract_tags(page):

            # get soup of a page
            response = requests.get(PDFHandler.URL + str(page))
            soup = BeautifulSoup(response.content, "html.parser")

            # find all games tags on a page
            tag_results = soup.find_all(
                class_="btn btn-sm btn-secondary mb-1",
                title="In "+language
            )

            return tag_results

        # loop over all pages
        for page in range (MAX_SEARCH_PAGE+1):
            print("Extracting URLs and titles from page:", page)

            # extract tags
            tags = _extract_tags(page)

            # loop over games in tags
            for game in tags:

                # extract {url, title}
                url = game.get("href")
                title = _extract_title(url)

                # add to self. games_info_list
                self.games_list.append({
                    "title": title,
                    "url": url
                })
                print(title, "was added to games_list")

        print(30*'-',
              str(len(self.games_list)) + "games have been added in total",
              sep="\n")


if __name__ == "__main__":

    handler = PDFHandler()
    handler.extract_games_list()
