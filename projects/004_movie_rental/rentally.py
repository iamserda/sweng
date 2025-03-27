import os
import csv
from customer import Customer
from movie import Movie


class Rentally:
    unique = False

    def __init__(self):
        if not Rentally.unique:
            # movies avail  and rented
            self.library = {}  # {movie.id: Movie-obj,...}
            self.customers = {}  # {customer_id : Customer-object,...}
            self.available_movies = set()  # a set of Movie.id
            self.rented_movies = {}  # {movie_id: customer_id,...}
            unique = True
        else:
            raise PermissionError(
                "Only 1 instance of this class is permitted at any time."
            )

    # CUSTOMER METHODS
    def add_customer(self, name: str):
        try:
            if not self.customers.keys():
                self.create_db("customer_db.csv")
            if not name:
                raise ValueError(
                    f"value: {name} is NOT a valid. Must be alphabetic string."
                )

            customer = Customer(name)
            self.customers[customer.customer_id] = customer
            customer.save_to_db()
            return customer

        except Exception as err:
            print(f"Error: {err}")
            pass  # TODO: handle specific Exceptions types etc...

    def add_movie(self, title, director=None):
        new_movie = Movie(title, director)
        if new_movie.id in self.library:
            raise ValueError(
                "ID-ERROR: This ID already exist in this library. Check ID and try again."
            )
        self.library[new_movie.id] = new_movie
        self.available_movies.add(new_movie.id)
        return new_movie.id

    def get_customer(self):
        customer_id = int(input("Enter Customer ID: "))
        customer = self.customers.get(customer_id)
        if not isinstance(customer, Customer):
            print(f"A Customer with id: {customer_id} was not found!")
        return customer

    def get_movie_id(self) -> int:
        movie_id = int(input("Enter Movie ID: "))
        if movie_id in self.rented_movies:
            return movie_id
        return -1

    def remove_customer(self):
        customer = self.get_customer()
        if isinstance(customer, Customer):
            self.customers.pop(customer.customer_id)
            print(f"Sucess: Removed a new customer with id: {customer.customer_id}")
        else:
            print(f"Failure: No customer found with given ID")

    # MOVIE METHODS

    def remove_movie(self, movie_id):
        if movie_id in self.rented_movies:
            print(f"Cannot remove {movie_id} from system because it is rented.")
        elif movie_id in self.library:
            if self.available_movies:
                del self.available_movies[movie_id]
            del self.library[movie_id]
            print(f"Sucess: {movie_id} was deleted from library.")

    def rent_a_movie(self):
        print("\nRent-A-Movie:")
        movie_id = int(input("Enter Movie ID: "))
        if movie_id not in self.library:
            print(
                f"A movie with ID: {movie_id} was NOT FOUND.\nTry searching for that title."
            )
        elif movie_id in self.rented_movies:
            print(f"Sorry, Movie: {movie_id} is NOT AVAILABLE at the moment!")
        else:
            try:
                customer: Customer = self.get_customer()
                self.available_movies.remove(movie_id)
                self.rented_movies[movie_id] = customer.customer_id
                customer.rented.add(movie_id)
                print(
                    f"Success: customer: {customer.customer_id} rented movie: {movie_id}"
                )
            except LookupError as err:
                print(err)
            except Exception as err:
                print(f"UnknownError: {err}")

    def return_a_movie(self) -> bool:
        try:
            movie_id = int(input("Enter Movie ID: "))
            customer = self.get_customer()
            if movie_id not in self.rented_movies:
                raise KeyError(
                    f"Error: Movie ID: {movie_id} is NOT in our Rented records."
                )
            if customer.customer_id != self.rented_movies.get(movie_id):
                raise KeyError(
                    "Error: This customer ID does not match our records for this rental."
                )
            customer.rented.remove(movie_id)
            self.rented_movies.pop(movie_id)
            self.available_movies.add(movie_id)
            print(
                f"Success: Customer: {customer.customer_id} has successfully returned movie: {movie_id}. Thank you!"
            )
        except KeyError as err:
            print(err)
        except Exception as err:
            print(err)

    def search_by_title(self, movie_title):
        for movie in self.library.values():
            if movie_title == movie.title:
                return movie

    def show_customer(self):
        print(self.customers.key())

    def create_db(self, csv_file_name):
        abs_path = os.path.abspath("./")
        file_path = os.path.join(
            abs_path, f"projects/004_movie_rental/data/{csv_file_name}"
        )
        if os.path.exists(file_path):
            with open(file_path, "w", newline="") as cust_db:
                header = ["id", "name", "rented"]
                writer = csv.DictWriter(cust_db, fieldnames=header)
                writer.writeheader()
