from Entities import Movie
from Scraper import Scraper
from config import urls, csv_files

import re

TAG_DICT = {'tag': 'td', 'tag_attr': 'overview-top'}


class MoviesScraper(Scraper):
    """
    A class for web scraping of movies information.
    """

    def __init__(self, url, file_name):
        """
        A constructor of a MoviesScraper object.
        :param url: the url address to scrape from.
        :param file_name: the file of the name where the output should be redirected to.
        """
        Scraper.__init__(self, url, file_name, "movies")


# todo: unify the common behavior across the different versions of get_movies functions (in the child classes)?
# todo: maybe use constants for the hard_coded URLs?
# todo: maybe we don't actually need "MoviesScraper" and "CelebsScraper" and it's enough to inherit the
# todo: specific classes directly from "Scraper? At this point the level of those two first mentioned it's not in use.

class NowInTheatersScraper(MoviesScraper):
    """
    A class that inherits the generic MoviesScraper for scraping the information of the movies currently in theaters
    according to IMDB webpage.
    """

    def __init__(self):
        MoviesScraper.__init__(self, urls["now_in_theaters"], csv_files["now_in_theaters"])

    def get_entities(self):
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


class TopRatedScraper(MoviesScraper):
    """
    A class that inherits the generic MoviesScraper for scraping the information of the 250 top rated movies
    in IMDB web page.
    """

    def __init__(self):
        MoviesScraper.__init__(self, urls["top_250"], csv_files["top_250"])

    def get_entities(self):
        soup = MoviesScraper.get_soup(self)
        movies_list = []
        movies_tags = [elem for elem in soup.find_all('a') if elem.has_attr("title") and "dir" in elem.attrs["title"]]
        years_tags = soup.find_all("span", {"class": "secondaryInfo"})
        for i in range(len(movies_tags)):
            name = movies_tags[i].get_text()
            director_and_actors = movies_tags[i].attrs["title"]
            href = movies_tags[i].attrs["href"]
            id = href[href.find("/", 2) + 1:-1]
            director = director_and_actors[:director_and_actors.find("(dir.)") - 1]
            year = years_tags[i].get_text()[1:-1]
            movies_list.append(Movie(name, year=year, imdb_id=id))
        return movies_list
