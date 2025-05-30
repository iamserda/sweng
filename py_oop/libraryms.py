class Library:
    def __init__(self):
        self.available_books = []
        self.borrowed_books = []
        self.current_acconts = []
        self.closed_accounts = []

    def add_book(self, title: str, author: str = "", count: int = 1):
        for index, book in enumerate(self.available_books):
            if title == book["title"]:
                self.available_books[index]["count"] += count
                break
        else:
            new_book = {"title": title, "author": author, "count": count, "borrowed": 0}
            self.available_books.append(new_book)

    def remove_book(self, title: str) -> bool:
        for i, book in enumerate(self.available_books):
            if title == book["title"]:
                print(f"Deleting book: {book} from Library.")
                self.available_books = (
                    self.available_books[:i] + self.available_books[i + 1 :]
                )
                return True
        return False

    def borrow_book(self, title):
        if not self.available_books:
            print(f"There are no books in this library system.")
        for book in self.available_books:
            if book["title"] == title:
                if book["count"] < 1:
                    print(
                        f"This '{title}' is not available currently. Sorry for the inconvenience."
                    )
                    # raise system alert to admin that book is no longer available.
                    return
                book["count"] -= 1
                book["borrowed"] = 1
                self.borrowed_books.append(title)
                print("success")

    def return_book(self, title):
        try:
            index = self.borrowed_books.index(title)
            del self.borrowed_books[index]
            for book in self.available_books:
                if book["title"] == title:
                    book["count"] += 1
            print("Message: Return accepted! Thank you!")
            print(f"Logging: Accepted return for title: {title}")
        except ValueError as err:
            print("Message: This title was not borrowed from our library.")
            print(f"Logging: {err}")

    def display_books(self):
        print(f"\tID#\t\tTitle:\t\tAuthor:\t\tCopies:")
        for index, book in enumerate(self.available_books):
            print(
                f"\t{index + 1}.\t\t{book['title']}\t\t{book['author']}\t\t{book['count']}"
            )

    def create_customer_account(self):
        pass

    def close_customer_account(self):
        pass


def show_menu():
    menu = """1. show menu\n2. add book\n3. remove book\n4. borrow book\n5. return book\nx. end game\n"""
    print(menu)


def start():
    lib_admin = Library()
    show_menu()
    while True:
        user_selected = input("{-: ")
        user_selected = (
            int(user_selected) if user_selected.isnumeric() else user_selected.lower()
        )
        match user_selected:
            case 1:
                show_menu()
            case 2:
                print("Adding a new book:")
                title = input("Enter the book's title: ")
                author = input("Enter the book's author: ")
                count = input("Enter total number of copies we have: ")
                count = int(count) if count.isnumeric() else 0
                if len(title) > 0 and count > 0:
                    new_book = {"title": title, "author": author, "count": count}
                    lib_admin.add_book(title=title, author=author, count=count)
                    print("Message: Sucessfully added a new book.")
                    if lib_admin.available_books:
                        lib_admin.display_books()
            case 3:
                print("Removing a book:")
                title = input("Enter the book's title: ")
                lib_admin.remove_book(title)
                if lib_admin.available_books:
                    lib_admin.display_books()
            case 4:
                print("Borrowing a book:")
                title = input("Enter the book's title: ")
                lib_admin.borrow_book(title)
                if lib_admin.available_books:
                    lib_admin.display_books()
            case 5:
                print("Returning a book:")
                title = input("Enter the book's title: ")
                lib_admin.remove_book(title)
                if lib_admin.available_books:
                    lib_admin.display_books()
            case "x":
                return
            case _:
                print("Invalid Selection")


if __name__ == "__main__":
    start()
