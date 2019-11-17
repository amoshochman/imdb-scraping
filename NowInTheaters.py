import os
import re
import csv
import requests
from datetime import date
from bs4 import BeautifulSoup
from Movie import Movie
from MoviesScraper import MoviesScraper

TAG_DICT = {'tag': 'td', 'tag_attr': 'overview-top'}


class NowInTheaters(MoviesScraper):
    def __init__(self):
        MoviesScraper.__init__(self, 'https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth', "now_in_theaters.csv")


    def get_movies(self):
        soup = MoviesScraper.get_soup(self)
        movies_list = []
        movies_tags = soup.find_all(TAG_DICT['tag'], attrs={'class': TAG_DICT['tag_attr']})
        for movie in movies_tags:
            h4_tag = movie.find('h4')
            movie_id = h4_tag.next.attrs["href"][7:-1]

            title = re.findall(r'title="(.*)"', str(h4_tag))
            title = re.match(r'^(.*) \((19\d\d|20\d\d)\)$', title[0])
            movie_name = title.group(1)
            movie_year = int(title.group(2))
            movies_list.append(Movie(movie_name, movie_year, movie_id))
        return movies_list
    