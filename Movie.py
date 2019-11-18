class Movie:
    """
    A very simple class representing a movie: name, id, director, etc.
    """

    def __init__(self, name, year, id, director=None):
        self.name = name
        self.year = year
        self.director = director
        self.id = id

    def __str__(self):
        return self.name + ", " + str(self.year) + ", " + self.director

    def to_list(self, include_id=False):
        l = []
        l.append(self.name)
        l.append(self.year)
        l.append(self.director)
        if include_id:
            l.append(self.id)
        return l
