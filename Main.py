#from BirthdayCelebs import BirthdayCelebs
from BirthdayCelebs import BirthdayCelebs
from MoviesScrapers import TopRated, NowInTheaters


def main():
    """
    A simple test of the web scraping from two different sections of IMDB webpage.
    """
    top_rated_scraper = TopRated()
    movies = top_rated_scraper.get_movies()
    header=movies[0].get_header()
    top_rated_scraper.write_to_csv(header, movies)

    now_in_theaters = NowInTheaters()
    movies = now_in_theaters.get_movies()
    header=movies[0].get_header()
    now_in_theaters.write_to_csv(header, movies)

    birthday_celebs = BirthdayCelebs()
    celebs=birthday_celebs.get_celebs()
    header=celebs[0].get_header()
    birthday_celebs.write_to_csv(header, celebs)

if __name__ == "__main__":
    main()
