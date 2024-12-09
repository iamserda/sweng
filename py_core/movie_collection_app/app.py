movies = []
deleted_movies = []

"""
{
    "title": "some name",
    "director": "director-name",
    "release": "12-22-2024",
}
"""


# add new movies
def add_new_movie(collection:list)->None:
    print("1 - Add a new movie to your movie collection.")
    movie = {
        "title": None,
        "director": None,
        "release": None
    }
    keys = list(movie.keys())
    messages = [f"Enter movie {keys[0]}: ", \
                f"Enter movie {keys[1]}: ", \
                f"Enter movie {keys[2]} year[YYYY]: "]
    
    for index, message in enumerate(messages):
        user_input = ""
        while not user_input:
            user_input = input(message)
        movie[keys[index]] = user_input
    movies.append(movie)

def display_collection(collection: list)->None:
    print("2 - Display the Movie Collection")
    try:
        if not collection:
            raise ValueError("Sorry, your collection is empty at the movie!")
        for movie in collection:
            print(f"Movie -> Title: {movie["title"]}, Director: {movie["director"]}, Release Date: {movie["release"]}.")
    except ValueError as err:
        print("Exception occured with this request! Please see details below.")
        print(f"Error: {err}. You will need to add movies to your collection first before you can view them.")

def basic_search(collection: list)->list:
    print("3 - Seach...")
    search_results = []
    user_input = input("Enter movie title to lookup: ")
    for movie in collection:
        if user_input in movie["title"]:
            search_results.append(movie)
    return search_results

def exectutor(option: int) -> None:
    
    if option == 1:
        # add new movies to the collection
        add_new_movie(movies)
    if option == 2:
        # Show all movies in the collection:
        display_collection(movies)
    if option == 3:
        # search then display:
        search_results = basic_search(movies)
        display_collection(search_results)

def app_menu():
    message = """
SELECT:
1 - Add a new movie to your movie collection
2 - Display the Movie Collection
3 - Search for the collection
x - exit, or X - exit
$:"""
    options = {"1", "2", "3", "x"}
    while True:
        user_input = input(message)
        if user_input.lower() not in options:
            print("Invalid selection! Try again")
            continue
        if user_input.lower() == "x":
            print("Exiting at user's request. Terminating...")
            break
        exectutor(int(user_input))

if __name__ == "__main__":
    app_menu()