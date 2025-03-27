from rentally import Rentally


def initial_db_seeding(system: Rentally):
    """Takes a Rentally-object, uses it to add new movies and customers to the app."""
    movies = [
        {"title": "Inception", "director": "Christopher Nolan"},
        {"title": "Pulp Fiction", "director": "Quentin Tarantino"},
        {"title": "The Grand Budapest Hotel", "director": "Wes Anderson"},
        {"title": "Parasite", "director": "Bong Joon-ho"},
        {"title": "The Godfather", "director": "Francis Ford Coppola"},
        {"title": "Spirited Away", "director": "Hayao Miyazaki"},
        {"title": "Get Out", "director": "Jordan Peele"},
        {"title": "Titanic", "director": "James Cameron"},
        {"title": "The Social Network", "director": "David Fincher"},
        {"title": "Mad Max: Fury Road", "director": "George Miller"},
    ]
    famous_people = [
        {"name": "Albert Einstein"},
        {"name": "Marie Curie"},
        {"name": "Leonardo da Vinci"},
        {"name": "Nelson Mandela"},
        {"name": "Amelia Earhart"},
        {"name": "Barack Obama"},
        {"name": "Frida Kahlo"},
        {"name": "Stephen Hawking"},
        {"name": "Ada Lovelace"},
        {"name": "Martin Luther King Jr."},
    ]

    for movie in movies:
        system.add_movie(**movie)

    for people in famous_people:
        system.add_customer(**people)


if __name__ == "__main__":
    system = Rentally()
    initial_db_seeding(system)
