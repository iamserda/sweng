def challenge1():
    def divide_numbers(a: int, b: int) -> None:
        try:
            print(a / b)
        except:
            print("An error occurred!")

        # do not modify below this line
        divide_numbers(10, 2)
        divide_numbers(12, 3)
        divide_numbers(2, 0)

def challenge2():
    def divide_numbers(a: str, b: str) -> None:
        try:
            print(int(a) / int(b))
        except Exception as error:
            print(f"An error occurred: {error}")



    # do not modify below this line
    divide_numbers("10", "2")
    divide_numbers("12", "0")
    divide_numbers("2", "not a number")

def challenge3():
    """    
    Expected output:
        5.0
        Error: Division by zero!
        Error: Invalid value!
    """
    def divide_numbers(a: str, b: str) -> None:
        try:
           print(int(a) / int(b))
        except ValueError:
            print("Error: Invalid value!")
        except ZeroDivisionError:
            print("Error: Division by zero!")    
        except Exception as error:
            print("An error occurred:", error)


    # do not modify below this line
    divide_numbers("10", "2")
    divide_numbers("12", "0")
    divide_numbers("2", "not a number")


# Testing
print("Challenge 1: ")
challenge1()

print("\nChallenge 2: ")
challenge2()

print("\nChallenge 3: ")
challenge3()