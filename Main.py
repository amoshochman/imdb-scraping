from TopRated import TopRated
from NowInTheaters import NowInTheaters


def main():
    top_rated_scraper = TopRated()
    movies = top_rated_scraper.get_movies()
    top_rated_scraper.write_to_csv(movies)

    now_in_theaters = NowInTheaters()
    movies = now_in_theaters.get_movies()
    now_in_theaters.write_to_csv(movies)


if __name__ == "__main__":
    main()
