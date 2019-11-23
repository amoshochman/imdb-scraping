from BirthdayCelebs import BirthdayCelebs
from MoviesScrapers import TopRated, NowInTheaters
from datetime import datetime

def main():
    """
    A test of the web scraping from some different sections of IMDB webpage.
    """
    top_rated_scraper = TopRated()
    movies = top_rated_scraper.get_movies()
    header=movies[0].get_header()
    top_rated_scraper.write_to_csv(header, movies)

    now_in_theaters = NowInTheaters()
    movies = now_in_theaters.get_movies()
    header=movies[0].get_header()
    now_in_theaters.write_to_csv(header, movies)

    today=datetime.today()
    birthday_celebs = BirthdayCelebs(str(today.month), str(today.day))
    celebs=birthday_celebs.get_celebs()
    header=celebs[0].get_header()
    birthday_celebs.write_to_csv(header, celebs)

if __name__ == "__main__":
    main()
