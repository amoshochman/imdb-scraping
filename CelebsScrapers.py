from Scraper import Scraper
from Entities import Celeb


class CelebsScraper(Scraper):
    """
    A generic class for web scraping of celebs information.
    """

    def __init__(self, url, file_name):
        """
        A constructor of a MoviesScraper object.
        :param url: the url address to scrape from.
        :param file_name: the file of the name where the output should be redirected to.
        """
        Scraper.__init__(self, url, file_name, "celebs")


class BirthdayScraper(CelebsScraper):
    """
    A class that inherits the generic MoviesScraper for scraping the information of the movies currently in theaters
    according to IMDB webpage.
    """

    def __init__(self, month, day):
        CelebsScraper.__init__(self,
                               'https://www.imdb.com/search/name/?birth_monthday=' + month + '-' + day + '&ref_=nv_cel_brn',
                               "celebs.csv")

    def get_entities(self):
        """
        Return a list of Celeb objects with basic information about them. One object per each celeb in
        "url" member.
        :return: a list of Celeb objects.
        """
        # todo: unify the common behavior across the different versions of get_movies functions (in the child classes).
        soup = CelebsScraper.get_soup(self)
        celebs_list = []
        celebs_tags = soup.find_all("div", attrs={"class": "lister-item-content"})
        for celeb in celebs_tags:
            a_tag = celeb.find('a')
            name = a_tag.get_text().strip()

            href_tag = a_tag.attrs["href"]
            id = href_tag[href_tag.find("/", 2) + 1:]

            celebs_list.append(Celeb(name,id))
        return celebs_list
