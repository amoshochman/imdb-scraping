class Entity:
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

    def __init__(self, name, year, id, director=None):
        self.name = name
        self.year = year
        self.director = director
        self.id = id


class Celeb(Entity):
    """
    A class representing a celeb: name, id, role, etc.
    """

    def __init__(self, id, name, role):
        self.name = name
        self.id = id
        self.role = role

