class Entity:
    """
    A class representing an entity from IMDB: movie, celeb, etc.
    """

    def to_list(self):
        members = self.get_header()
        members_values = []
        for member in members:
            members_values.append(getattr(self, member))
        return members_values


    def get_header(self):
        return [member for member in dir(self) if not member.startswith('__') and not callable(getattr(self, member))]


class Movie(Entity):
    """
    A class representing a movie: name, id, director, etc.
    """

    def __init__(self, name, year, imdb_id):
        self.name = name
        self.year = year
        self.imdb_id = imdb_id

class Celeb(Entity):
    """
    A class representing a celeb: name, id, role, etc.
    """

    def __init__(self, name, imdb_id):
        self.name = name
        self.imdb_id = imdb_id


class CelebToMovie(Entity):

    def __init__(self, movie_id, celeb_id, role_id):
        self.movie_id = movie_id
        self.celeb_id = celeb_id
        self.role_id = role_id
