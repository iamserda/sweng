"""importing datetime module"""
import datetime
import random
from helpers import select_card, generate_card, master_factory, amex_factory, visa_factory

scapital_clients = {}
amex_issued_set = set()
visa_issued_set = set()
master_issued_set = set()




def issue_card(user_credit):
    """issue card based on credit"""
    if user_credit < 300 or user_credit > 850:
        print("One of our Client Concierge will be with your shorty!")
        return None

    if user_credit >= 720:
        print("Excellent, we can offer you the Deluxe AMEX card.\nProcessing....\n")
        return select_card("amex")

    if user_credit >= 690:
        print("Great, we can offer you our Premium VISA card.\nProcessing....\n")
        return select_card("visa")

    if user_credit >= 630:
        print(
            "Awesome, we can offer you own of our Premium MASTERCard.\nProcessing....\n"
        )
        return select_card("master")


def get_servicers():
    """returns an object of card servicers available at the firm"""
    return {
        "amex": {"function": amex_factory, "issued": amex_issued_set},
        "visa": {"function": visa_factory, "issued": visa_issued_set},
        "master": {"function": master_factory, "issued": master_issued_set},
    }


def get_user_info(new_user=True):
    """prompt user for information to create account"""
    if new_user:
        print(f"System Time: {datetime.datetime.now()}")
        fname = input("Enter your first name: ")
        lname = input("Enter your last name: ")
        username, pwd = create_user_profile()
        m, d, y = input("Enter DOB: MM-DD-YYYY: ").split("-")
        dob = datetime.datetime(year=int(y), month=int(m), day=int(d))
        credit_score = int(input("Enter your FICO score: "))

    scapital_clients[username]["first"] = fname
    scapital_clients[username]["last"] = lname
    scapital_clients[username]["dob"] = dob
    scapital_clients[username]["password"] = pwd
    scapital_clients[username]["credit_score"] = credit_score

    return username


def create_user_profile():
    """creates user profile"""
    username = input("Enter your username: ")

    while username in scapital_clients.keys():
        print("This username already exist, please try again")
        username = input("Enter your username: ")

    pwd_constraints = "Passwords must be: 8 characters long and alphanumeric."
    password = input(pwd_constraints + "\nEnter your password: ")
    while not password or len(password) <= 8 or not str(password).isalnum():
        password = input("Enter your password: ")
    scapital_clients[username] = {"user": username, "pwd": password}
    return username, password


def start_app(start=False):
    if start:
        print("Welcome to Simus Capital Premium Cards Service!")
        username = get_user_info()
        user_data = scapital_clients[username]
        fname = user_data["first"]
        greeting = f"Hi {fname}!"
        print(greeting)
        print()
        print("Accessing credit history...")
        card_issued = issue_card(user_data["credit_score"])
        # print(card_issued)s
        if card_issued is None:
            print(
                "Please provide your local contact phone number,\nand a member of our client concierge will reach out to you\nwithin 60 minutes."
            )
            contact_number = input()
            scapital_clients[username]["phone"] = (
                contact_number
                if len(contact_number) >= 8
                else "".join("555-555-5555".split("-"))
            )
            print(f"{scapital_clients[username]["first"]}, thank you for using S Capital as your preferred financial institution.")
            print(f"Our team will review your account and get back to you within 30 days.")
            print(f"We will contact you at {scapital_clients[username]["phone"]}")
            return
        scapital_clients[username]["card1"] = card_issued
        print("Congratulations!")
        print("Welcome to the Simus Capital card-holders family!")
        print(f"Your new car number is {scapital_clients[username]['card1']}")

if __name__ == "__main__":
    start_app(start=True)
