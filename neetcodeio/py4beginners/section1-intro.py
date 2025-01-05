from decimal import Decimal, getcontext

def challenge1():
    print("Hello, world!")

def challenge2():
    def calculate_pi(n):
        getcontext().prec = n + 2  # Set precision higher than needed for accuracy
        
        C = 426880 * Decimal(10005).sqrt()
        K = 6
        M = 1
        X = 1
        L = 13591409
        S = L
        
        for i in range(1, n):
            M = (K ** 3 - 16 * K) * M // i ** 3
            L += 545140134
            X *= -262537412640768000
            S += Decimal(M * L) / X
            K += 12
        
        pi = C / S
        return str(pi)[:n + 2]  # Return first n digits plus the '3.'

    n = 20
    pi_digits = calculate_pi(n)
    print(pi_digits)

def challenge3():
    print("Fifth")
    print("Fourth")
    print("Sixth")
    
def challenge4():
    print("My favorite quote is \"To be or not to be.\"")
    

def challenge5():
    # fix this: print("Can someone pls add a closing parenthesis?"
    print("Can someone pls add a closing parenthesis?")

def challenge6():
    """
    Your task is to fix the code on the right without deleting any of the lines. It should print the following text to the console:

    I belong here.
    I also belong here.
    Me too!
    """
    print("I belong here.")
    print("Why am I here?")
    print("Get me out of here!")
    print("I also belong here.")
    print("Me too!")