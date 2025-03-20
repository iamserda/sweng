class Movie:
    price = 10.00
    new_id = 1

    def __init__(self, title, director):
        self._id = new_id
        self._title = title
        self._director = director
        new_id += 1


class Customer:
    def __init__(self, name):
        self._name = name
        self.borrowed = set()
        self.history = []

    def borrow_movie(self, movie: Movie):
        self.borrowed.add(movie.movie_id)

    def return_movie(self, movie: Movie):
        if movie.movie_id in self.borrowed:
            self.history.append(movie.movie_id)
            self.borrowed.remove(movie.movie_id)
            return "success"
        else:
            return "failed: Unable to complete this tasks. Movie is not in this user's borrowing profile."
