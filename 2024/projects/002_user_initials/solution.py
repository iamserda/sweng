def main() -> None:
    print("Please enter your First, Middle, and Last name!")
    first_name = input("First: ")
    middle_name = input("Middle: ")
    last_name = input("Last: ")
    first_initial = first_name[0]
    middle_initial = "" if not middle_name else middle_name[0]
    last_initial = last_name[0]

    return f"Your initials are {first_name[0]}.{name[0]}"
