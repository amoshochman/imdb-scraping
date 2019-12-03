class Entity:
    """
    A class representing an entity from IMDB: movie, celeb, etc.
    """

    def to_list(self):
        """
        Returns a list with the members of the object. As this function calls function get_header(), it is guaranteed
        that both functions will return the members and the values for them in the same order.
        :return: a list.
        """
        members = self.get_header()
        members_values = []
        for member in members:
            members_values.append(getattr(self, member))
        return members_values

    def get_header(self):
        """
        Returns a list with the names of the members of the object.
        :return: a list.
        """
        return [member for member in dir(self) if not member.startswith('__') and not callable(getattr(self, member))]


class Movie(Entity):
    """
    A class representing a movie: name, id, year, etc.
    """

    def __init__(self, name, year, imdb_id):
        self.name = name
        self.year = year
        self.imdb_id = imdb_id


class Celeb(Entity):
    """
    A class representing a celeb: name, id, etc.
    """

    def __init__(self, name, imdb_id):
        self.name = name
        self.imdb_id = imdb_id


class CelebToMovie(Entity):
    """
    A class representing a connection between a movie and a celeb.
    That is, an instance of this class will mean that self.celeb_id is part of the cast of self.movied_id
    as a role_id (which can correspond to actor, director, producer, editor, etc.)
    """

    def __init__(self, movie_id, celeb_id, role_id):
        self.movie_id = movie_id
        self.celeb_id = celeb_id
        self.role_id = role_id


class Role(Entity):
    """
    A class representing a role in a movie: actor, director, producer, editor, etc.
    """

    def __init__(self, role_name):
        self.role_name = role_name
