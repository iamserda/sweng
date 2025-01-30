def challenge1():
    message = "Hello, world!"
    # don't modify the code below this line
    print(message)
    print(message)

def challenge2():
    """
    Fix this:
    1capital_of_spain = "Madrid"
    print(capital_of_france)
    print(capital_of_germany)
    """
    capital_of_spain = "Madrid"
    capital_of_france = "Paris"
    capital_of_germany = "Berlin"
    
    print(capital_of_spain)
    print(capital_of_france)
    print(capital_of_germany)
    

def challenge3():
    """ Covert to snake_case:
    
    pythonCreationDate = "February, 1991"
    javaCreationDate = "May, 1995"
    javascriptCreationDate = "December, 1995"

    print(python_creation_date)
    print(java_creation_date)
    print(javascript_creation_date)
    """
    python_creation_date = "February, 1991"
    java_creation_date = "May, 1995"
    javascript_creation_date = "December, 1995"

    print(python_creation_date)
    print(java_creation_date)
    print(javascript_creation_date)



def challenge4():
    """
    Expected Output:
    The first message
    The second message
    The third message
    """
    message = "The first message"
    print(message)
    message = "The second message"
    print(message)
    message = "The third message"
    print(message)

def challenge5():
    """
    Expected Output:
    The first message
    The second message
    The third message
    """
    msg1, msg2 = "World", "Hello"
    msg3, msg4, msg5 = "Name", "Is", "My"
    # Don't change the code above this line
    msg1, msg2 = msg2, msg1
    msg3, msg4, msg5 = msg5, msg3, msg4
    # Don't change the code below this line
    print(msg1) # Hello
    print(msg2) # World
    print(msg3) # My
    print(msg4) # Name
    print(msg5) # Is
    
def challenge6():
    """< see expected output>"""
    integer_type = 1
    float_type = 2.0
    bool_type = False
    string_type = "string_type"
    list_type = list("list_type")
    
    print(type(integer_type)) # <class 'int'>
    print(type(float_type)) # <class 'float'>
    print(type(bool_type)) # <class 'bool'>
    print(type(string_type)) # <class 'str'>
    print(type(list_type)) # <class 'list'>

def challenge7():
    variable = 1
    print(type(variable)) # <class 'int'>
    variable = 2.0
    print(type(variable)) # <class 'float'>
    variable = False
    print(type(variable)) # <class 'bool'>
    variable = "string_type" 
    print(type(variable)) # <class 'str'>
    variable = list("list_type")
    print(type(variable)) # <class 'list'>


# Execution
challenge1()
challenge2()
challenge3()
challenge4()
challenge5()
challenge6()
challenge7()