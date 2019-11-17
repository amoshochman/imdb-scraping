import csv
import requests
from bs4 import BeautifulSoup

class MoviesScraper:
    def __init__(self, url, file_name):
        self.url = url
        self.file_name = file_name

    def get_soup(self):
        """
        Uses the object member url to read/scrape the associated web page and returns a BeautifulSoup object
        that contains all the movies that are listed in the given url.
        The tags that are used as markers in the html script depend on the web page.
        :return: A BeautifulSoup object.
        """
        page = requests.get(self.url)
        return BeautifulSoup(page.content, 'html.parser')

    def write_to_csv(self, movies):
        """
        Takes a list of Movie objects and writes them to a csv file with the name of the file_name member.
        :param movies: a list of Movie objects.
        """
        with open(self.file_name, 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(["Name", "Year", "Director"])
            writer.writerows([movie.to_list() for movie in movies])
        csvFile.close()
