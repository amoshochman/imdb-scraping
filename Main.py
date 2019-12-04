from CelebsScrapers import BirthdayScraper
from datetime import datetime

from MoviesScrapers import TopRatedScraper, NowInTheatersScraper
from datetime import datetime
import sys
import argparse

def get_valid_date(string):
    try:
        return datetime.strptime(string, "%d/%m")
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(string) + " Please enter it in format 'DD/MM'."
        raise argparse.ArgumentTypeError(msg)

def main():
    """
    Some tests for IMDB Web scraping.
    """
    #todo: add argument for the file names.
    #todo: add selects, etc.
    parser = argparse.ArgumentParser(description="---=== An imdb web scraper ===---")

    parser.add_argument("-top", action='store_true',
                        help="Scrapes the top 250 rated movies.")

    parser.add_argument("-now", action='store_true',
                        help="Scrapes the movies now in USA theaters.")

    parser.add_argument("-celebs", action='store_true',
                        help="Scrapes the celebrities born today.\
                             Use [-d] to select a specific date")

    parser.add_argument("-db", action='store_true',
                        help="Saves the scraped data in the DB.")

    parser.add_argument("-csv", action='store_true',
                        help="Inserts the records in a CSV file.")

    parser.add_argument("-d", "--date", type=get_valid_date, nargs=1, default=None,
                        help="Perform web scarping to the celebrities born on this date.\n \
                                 Enter date in the format: 'DD/MM'")

    args = parser.parse_args()

    if not (args.csv or args.db) or not (args.top or args.celebs or args.now):
        parser.print_usage()
        print()
        print("At least one option needs to be chosen from both sets:")
        print("{-db, -csv}, {-top, -now, celebs}")
        print("If '-celebs' not present, a passed date will be ignored.")
        sys.exit(1)

    if args.top:
        top_rated_scraper = TopRatedScraper()
        movies = top_rated_scraper.get_movies()
        header = movies[0].get_header()
        if args.db:
            top_rated_scraper.write_to_db(header, movies)
        if args.csv:
            top_rated_scraper.write_to_csv(header, movies)

    if args.now:
        now_in_theaters_scraper = NowInTheatersScraper()
        movies = now_in_theaters_scraper.get_movies()
        header = movies[0].get_header()
        if args.db:
            now_in_theaters_scraper.write_to_db(header, movies)
        if args.csv:
            now_in_theaters_scraper.write_to_csv(header, movies)

    if args.celebs:
        if args.date:
            celeb_date = args.date[0]
        else:
            celeb_date = datetime.today()
        birthday_celebs_scraper = BirthdayScraper(str(celeb_date.month), str(celeb_date.day))
        celebs = birthday_celebs_scraper.get_celebs()
        header = celebs[0].get_header()
        if args.db:
            birthday_celebs_scraper.write_to_db(header, celebs)
        if args.csv:
            birthday_celebs_scraper.write_to_csv(header, celebs)


if __name__ == "__main__":
    main()
