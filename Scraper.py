import csv

import requests
from bs4 import BeautifulSoup
from DBUtils import DBConnector, DBCreator
from config import sql, tables


class Scraper:
    """
    A generic class for web scraping of IMDB information.
    """

    def __init__(self, url, file_name, table):
        """
        A constructor of a Scraper object.
        :param url: the url address to scrape from.
        :param file_name: the file of the name where the output should be redirected to.
        """
        self.url = url
        self.file_name = file_name
        self.table = table
        DBCreator.start_db(sql["host"], sql["user"], sql["passwd"], sql["db"], tables)
        self.my_connector = DBConnector(sql["host"], sql["user"], sql["passwd"], sql["db"])

    def get_soup(self):
        """
        Uses the object member url to read/scrape the associated web page and returns a BeautifulSoup object
        that contains all the content in the given url.
        The tags that are used as markers in the html script depend on the web page.
        :return: A BeautifulSoup object.
        """
        page = requests.get(self.url)
        return BeautifulSoup(page.content, 'html.parser')

    def write_to_csv(self, header, entities):
        """
        Takes a list of IMDB objects and writes them to a csv file with the name of the file_name member,
        using the provided header.
        :param header: the header to use in the CSV file.
        :param entities: a list of IMDB objects.
        """
        with open(self.file_name, 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(header)
            writer.writerows([entity.to_list() for entity in entities])
        csvFile.close()

    def write_to_db(self, header, entities):
        self.my_connector.insert(self.table, ', '.join(header), [entity.to_list() for entity in entities])

