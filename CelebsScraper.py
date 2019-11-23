import csv
import requests
from bs4 import BeautifulSoup

from Scraper import Scraper


class CelebsScraper(Scraper):
    """
    A generic class for web scraping of celebs information.
    """

    def __init__(self, url, file_name):
        """
        A constructor of a MoviesScraper object.
        :param url: the url address to scrape from.
        :param file_name: the file of the name where the output should be redirected to.
        """
        Scraper.__init__(self, url, file_name)
