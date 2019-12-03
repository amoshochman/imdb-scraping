from MoviesScrapers import TopRatedScraper, NowInTheatersScraper
from CelebsScrapers import BirthdayScraper
from datetime import datetime

def main():
    """
    A test of the web scraping from some different sections of IMDB webpage.
    """
    top_rated_scraper = TopRatedScraper()
    movies = top_rated_scraper.get_movies()
    header = movies[0].get_header()
    top_rated_scraper.write_to_csv(header, movies)
    top_rated_scraper.write_to_db(header, movies)

    now_in_theaters_scraper = NowInTheatersScraper()
    movies = now_in_theaters_scraper.get_movies()
    header = movies[0].get_header()
    now_in_theaters_scraper.write_to_csv(header, movies)
    now_in_theaters_scraper.write_to_db(header, movies)

    today = datetime.today()
    birthday_celebs_scraper = BirthdayScraper(str(today.month), str(today.day))
    celebs = birthday_celebs_scraper.get_celebs()
    header = celebs[0].get_header()
    birthday_celebs_scraper.write_to_csv(header, celebs)
    birthday_celebs_scraper.write_to_db(header, celebs)


if __name__ == "__main__":
    main()
