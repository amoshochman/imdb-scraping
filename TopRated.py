import requests
from bs4 import BeautifulSoup
from Movie import Movie
from MoviesScraper import MoviesScraper

#TAG_BEST_250 = {'tag': 'td', 'tag_attr': 'posterColumn'}
#Should we use it?

class TopRated(MoviesScraper):
    def __init__(self):
        MoviesScraper.__init__(self, 'https://www.imdb.com/chart/top', "top_250.csv")

    def get_movies(self):
        soup = MoviesScraper.get_soup(self)
        movies_list = []
        movies_tags = [elem for elem in soup.find_all('a') if elem.has_attr("title") and "dir" in elem.attrs["title"]]
        years_tags = soup.find_all("span", {"class": "secondaryInfo"})
        for i in range(len(movies_tags)):
            name = movies_tags[i].get_text()
            director_and_actors = movies_tags[i].attrs["title"]
            id = movies_tags[i].attrs["href"]
            director = director_and_actors[:director_and_actors.find("(dir.)") - 1]
            year = years_tags[i].get_text()[1:-1]
            movies_list.append(Movie(name, year, id, director))
        return movies_list
