class Movie:
    id_counter = 0

    def __init__(self, title: str, director: str) -> object:
        Movie.id_counter += 1
        self.id: int = Movie.id_counter
        self.title: str = title
        self.director: str = director

    def __str__(self):
        return f"id: {self.id}, title: {self.title}, director: {self.director}"
