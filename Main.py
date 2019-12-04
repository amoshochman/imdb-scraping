from CelebsScrapers import BirthdayScraper
from MoviesScrapers import TopRatedScraper, NowInTheatersScraper
from config import DATE_FORMAT

from datetime import datetime
import sys
import argparse


def get_human_format(date):
    return date.replace('%', '').replace('d', 'dd').replace('m', 'mm').replace('y', 'yy')


def get_valid_date(string):
    try:
        return datetime.strptime(string, "%d/%m")
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(string) + " Please enter it in format " + get_human_format(
            DATE_FORMAT)
        raise argparse.ArgumentTypeError(msg)


def write_records(scraper, db, csv):
    entities = scraper.get_entities()
    header = entities[0].get_header()
    if db:
        scraper.write_to_db(header, entities)
    if csv:
        scraper.write_to_csv(header, entities)


def get_scrapers(args):
    scrapers = []
    if args.top:
        scrapers.append(TopRatedScraper())
    if args.now:
        scrapers.append((NowInTheatersScraper()))
    if args.celebs:
        if args.date:
            celeb_date = args.date[0]
        else:
            celeb_date = datetime.today()
        scrapers.append(BirthdayScraper(str(celeb_date.month), str(celeb_date.day)))
    return scrapers


def get_args(parser):
    args = parser.parse_args()
    if not (args.csv or args.db) or not (args.top or args.celebs or args.now):
        parser.print_usage()
        print()
        print("At least one option needs to be chosen from both sets:")
        print("{-db, -csv}, {-top, -now, celebs}")
        print("If '-celebs' not present, 'date' will be ignored if present.")
        sys.exit(1)
    return args


def main():
    """
    Some tests for IMDB Web scraping.
    """
    # todo: add argument for the file names.
    # todo: add selects, etc.
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
                                 Enter date in format: " + get_human_format(DATE_FORMAT))

    args = get_args(parser)

    scrapers = get_scrapers(args)

    for scraper in scrapers:
        write_records(scraper, args.db, args.csv)


if __name__ == "__main__":
    main()
