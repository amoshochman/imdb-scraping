import re
from Entities import Movie, Celeb
#from MoviesScraper import MoviesScraper

TAG_DICT = {'tag': 'td', 'tag_attr': 'overview-top'}
from CelebsScraper import CelebsScraper


class BirthdayCelebs(CelebsScraper):
    """
    A class that inherits the generic MoviesScraper for scraping the information of the movies currently in theaters
    according to IMDB webpage.
    """

    def __init__(self):
        CelebsScraper.__init__(self, 'https://www.imdb.com/search/name/?birth_monthday=11-28&ref_=nv_cel_brn', "celebs.csv")
        #CelebsScraper.__init__(self, 'https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth',"celebs.csv")

    def get_celebs(self):
        """
        Return a list of Movie objects with basic information about them. One object per each celeb in
        "url" member.
        :return: a list of Movie object.
        """
        # todo: unify the common behavior across the different versions of get_movies functions (in the child classes).
        soup = CelebsScraper.get_soup(self)
        celebs_list = []
        #movies_tags = soup.find_all(TAG_DICT['tag'], attrs={'class': TAG_DICT['tag_attr']})
        celebs_tags = soup.find_all("div", attrs={"class": "lister-item-content"})
        for celeb in celebs_tags:
            a_tag=celeb.find('a')
            name=a_tag.get_text().strip()

            href_tag=a_tag.attrs["href"]
            id=href_tag[href_tag.find("/",2)+1:]

            p_tag=celeb.find('p')
            p_tag_text=p_tag.get_text()
            role=p_tag_text[:p_tag_text.find("|")].strip()

            celebs_list.append(Celeb(id, name, role))
        return celebs_list

