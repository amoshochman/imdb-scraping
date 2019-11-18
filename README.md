# IMDB Web Scraping

A project to practice Web Scraping using IMDB web page. 
At the very beginning, it deals with movies. That is, downloading basic information about movies and outputting to CSVs files. Later similar functionality will be implemented for other entities such as actors, ratings, etc.

## Structure

1. A very simple class representing a movie: name, id, director, etc.
2. A generic class for movie scraping, MoviesScraper.
3. Classes that inherit from MoviesScraper. At the beginning, for the pages with the 250 top rated movies and the one with the movies currently in theaters. Later on more child class will be added.
4. A very simple test, in file Main.py.

As it can be seen in Main.py, the currently standard way of using the project is creating an object from one of the classes inheriting from MoviesScraper and then using the object for:
- getting a list of movies.
- using that list for outputting the information to a CSV file.

When creating the object, the URL to scrape from and the name of the file to output need to be specified.

## Running the tests

In order to see and test the current functionality, run Main.py with no parameters.

## Authors
* **Amos Hochman**
* **David Tal**


