import csv
import os

class Customer:
    # class props
    _id = 0

    def __init__(self, name):
        Customer._id += 1
        self.customer_id = Customer._id
        self.name = name
        self.rented = set()  # set of Movie.id

    def __str__(self):
        return f"id: {self.customer_id} -- name: {self.name}"

    def as_dict(self):
        return {"id": self.customer_id, "name": self.name, "rented": list(self.rented)}

    def check_rented(self, movie_id):
        return movie_id in self.rented

    def get_rented(self):
        return self.rented

    def save_to_db(self):
        try:
            abs_path = os.path.abspath("./")
            file_path = os.path.join(abs_path, "data/customer_db.csv")
            with open(file_path, "a+", newline="") as cust_db:
                header = ["id", "name", "rented"]
                csv_scribe = csv.DictWriter(cust_db, fieldnames=header)
                csv_scribe.writerow(self.as_dict())
        except Exception as err:
            # TODO: Handle specific expection instead of generics.
            print(err)

if __name__ == "__main__":
    customer0 = Customer("Michael Jordan")
    customer1 = Customer("James Bond")
    customer0.rented.add(1)
    customer0.rented.add(2)
    customer1.rented.add(3)
    print(customer0, customer0.get_rented())
    print(customer1, customer1.get_rented())
