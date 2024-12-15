

def main()->None:
    one_km_to_mile:float = 0.621371
    try:
        kilometers:float = float(input("Enter number of Kilometers to be converted into miles: "))
        mile = one_km_to_mile * kilometers
        message_km = f"{kilometers} kilometers" if kilometers > 1 else f"{kilometers} kilometer"
        message_mi = f"{mile} miles" if mile > 1 else f"{mile} mile"
        print(f"{message_km} equals {message_mi}.")

    except ValueError as err:
        print(f"ValueError: {err}.\nExpecting float, received non-numeric type, or type that cannot be converted to float.\nTerminating app now!")
    except Exception as err:
        print(f"Exception: {err}")

if __name__ == "__main__":
    main()
    