class Movie:
    id_counter = 0

    def __init__(self, title: str, director: str) -> object:
        Movie.id_counter += 1
        self.id = Movie.id_counter
        self.title = title
        self.director = director

    def __str__(self):
        return f"id: {self.id}, title: {self.title}, director: {self.director}"


titanic = Movie("Titanic", "Joe Shmoe")
lion_king = Movie("The Lion King", "Timon, Pumba")

print(titanic)
print(lion_king)
