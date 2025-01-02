def greet_user(name: str) -> None:
    """ takes a string and prints a greeting to the user."""
    try:
        if not isinstance(name, str):
            raise ValueError("var 'name' is not a string")
        print(f"Hello, {name}")
    except ValueError as err:
        print("Error:", err)


# Tests
greet_user("Serda")
greet_user("Jameis")
