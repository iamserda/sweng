def greet_user(usr_name):
    """Given a string, user's name, prints the user's name"""
    if not isinstance(usr_name, str):
        raise TypeError(
            f"Expected data of type string. Receive {type(usr_name)}")
    if not usr_name:
        raise ValueError("Argument received was an empty string.")
    print(f"Hello, {usr_name}! Welcome to Python World!")


# TEST ARENA:
# greet_user("")
# greet_user(4)
# greet_user()
greet_user("Apollo")
