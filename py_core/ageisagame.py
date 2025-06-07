try:
    print(
        "You will be prompted to enter your age."
        "\nFor example, you should enter '18' if "
        "you are 18 years old."
    )
    age = int(input("Enter your age: "))
    if age < 0:
        raise (ValueError("Your age cannot be negative."))
    m1 = "You are{} {} year{} old!".format(
        " less than" if age < 1 else "",
        age + 1 if age < 1 else age,
        "s" if age > 1 else "",
    )
    print(m1)
except (ValueError, ZeroDivisionError) as err:
    print("An error occurred!")
    print("logging-error:", err)
else:
    # logging...
    print("Success!")
    print("no-logging!")
