sql = {'host': 'localhost', 'user': 'root', 'passwd': 'root', 'db': 'IMDB_Scraping'}

urls = {'top_250': 'https://www.imdb.com/chart/top',
        'now_in_theaters': 'https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth'}

csv_files = {'top_250': 'top_250.csv',
             'now_in_theaters': 'now_in_theaters.csv'}

tables = {"movies": "CREATE TABLE movies "
                    "(id INT AUTO_INCREMENT PRIMARY KEY, "
                    "imdb_id VARCHAR(255) UNIQUE, "
                    "name VARCHAR(255), year INT(4),"
                    "imdb_rating FLOAT,"
                    "rt_rating FLOAT,"
                    "mc_rating FLOAT)",

          "celebs": "CREATE TABLE celebs "
                    "(id INT AUTO_INCREMENT PRIMARY KEY, "
                    "imdb_id VARCHAR(255) UNIQUE, "
                    "name VARCHAR(255))",

          "roles": "CREATE TABLE roles "
                   "(id INT AUTO_INCREMENT PRIMARY KEY, "
                   "name VARCHAR(255))",

          "celebs_to_movies": "CREATE TABLE celebs_to_movies "
                              "(id INT AUTO_INCREMENT PRIMARY KEY, "
                              "celeb_id INT,"
                              "movie_id INT,"
                              "role_id INT,"
                              "FOREIGN KEY(celeb_id) REFERENCES celebs(id),"
                              "FOREIGN KEY(movie_id) REFERENCES movies(id),"
                              "FOREIGN KEY(role_id) REFERENCES roles(id))"}

omdb = {"prefix": "http://www.omdbapi.com/?", "key": "6e17b7f7", }

DATE_FORMAT = "%d/%m"

ratings_sources_names = {'Internet Movie Database': "imdb",
                         'Rotten Tomatoes': "rt",
                         'Metacritic': "mc"}
