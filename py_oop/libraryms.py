class Library:
    def __init__(self):
        self.available_books = []
        self.borrowed_books = []
        self.current_acconts = []
        self.closed_accounts = []

    def add_book(self, title: str, author, count: int = 1):
        new_book = {"title": title, "author": author, "count": count}
        for book in self.available_books:
            if new_book["title"] == book.title:
                book["count"] += 1
                break
        else:
            self.available_books.append(new_book)

    def remove_book(self, title: str):
        for i, book in enumerate(self.available_books):
            if title == book["title"]:
                print(f"Deleting book: {book} from Library.")
                del self.available_books[i]

    def borrow_book(self, title):
        for book in self.available_books:
            if book["title"] == title:
                if book["count"] < 1:
                    print(
                        f"Book '{title}' is not available at this time! Sorry for the inconvenience."
                    )
                    return
                book["count"] -= 1
                print("success")

    def return_book(self):
        pass

    def create_customer_account(self):
        pass

    def close_customer_account(self):
        pass


def show_customer_menu():
    menu = """
    1. show menu
    2. register
    3. sign-in
    4. borrow a book
    5. 
    x. 
    """
