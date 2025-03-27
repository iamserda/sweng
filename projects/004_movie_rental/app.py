from rentally import Rentally
from movie import Movie
from customer import Customer
from populate_data import test_populate


def show_menu():
    message = "\n1. Rent a Movie\n2. Return a Movie\n3. Add a Movie\n4. Delete a Movie\n5. Add a Customer\n6. Delete a Customer\nm. Show Menu\nx. Exit\n"
    print(message)


def start_game():
    show_menu()
    flag = True
    while flag:
        user_input = input("$: ")
        match user_input:
            case "1":
                system.rent_a_movie()
            case "2":
                system.return_a_movie()
            case "3":
                movie_title = input("Enter movie title: ")
                movie_director = input("Enter movie director's name: ")
                system.add_movie(title=movie_title, director=movie_director)
            case "4":
                print("WARNING: Selected 'Delete a Movie'")
                movie_id = int(input("Enter movie ID: "))
                system.remove_movie(movie_id)
            case "5":
                customer_name = input("Enter Customer's name: ")
                system.add_customer(name=customer_name)
            case "6":
                system.remove_customer()
            case "m":
                show_menu()
            case "x":
                flag = False
            case _:
                raise ValueError("Invalid input... terminating the app...")


if __name__ == "__main__":
    print("\nWelcome to Rentally:\n")
    system = Rentally()
    test_populate(system)
    start_game()
