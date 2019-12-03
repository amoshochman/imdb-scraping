# IMDB Web Scraping

A project to practice Web Scraping using IMDB web page. 
At the very beginning, it deals with movies. That is, downloading basic information about movies and outputting to CSVs files. Later similar functionality will be implemented for other entities such as actors, ratings, etc.

## Structure

1. Very simple classes representing entities, like for example:
- movie: name, id, year, etc.
- celeb: name, id, etc.
2. Classes for scraping: 
- Scraper is the upper one.
- From Scraper inherits MoviesScraper and CelebsScraper.
- From MoviesScraper inherits a class for scraping the top rated movies and another one for scraping
the movies currently in theaters in the USA.
- From CelebsScraper inherits a class for scraping the celebs that have born on any given day.
Later on more child class will be added.
3. A very simple test, in file Main.py.
4. DBUtils.py, that allows to run scripts and queries on the DB.

As it can be seen in Main.py, the currently standard way of using the project is creating an object from one of the classes inheriting from MoviesScraper and then using the object for:
- getting a list of movies.
- optionally using that list for outputting the information to a CSV file.
- optionally using that list for storing the information in the DB.

When creating the object, the URL to scrape from and the name of the file to output need to be specified.

## Running the tests

In order to see and test the current functionality, run Main.py with no parameters.

## Authors
* **Amos Hochman**
* **David Tal**


