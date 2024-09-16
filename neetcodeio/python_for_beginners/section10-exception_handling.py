def challenge1():
    pass

def challenge2():
    pass

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


challenge1()
challenge2()
challenge3()