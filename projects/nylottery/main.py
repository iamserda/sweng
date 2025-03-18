from random import randint
from helpers import *

def get_user_name():
    user_name = input("Enter your name: ")
    return user_name









def start_game():
    name = get_user_name()
    greeting(name)
    user_five, usr_mega = get_user_selection()
    lottery_five = generate_lottery_five()
    lottery_megaball = generate_mega_ball()
    announce_lottery(lottery_five, lottery_megaball)
    hits = verify_picks(lottery_five, user_five)
    number_of_matches = len(hits)
    msg, prize = get_prize(number_of_matches, lottery_megaball == usr_mega)
    print(f"Lottery 5-Picks: {lottery_five}")
    print(f"Your 5-Picks: {user_five}")
    if number_of_matches:
        print(f"You have matched {number_of_matches}")

    print(f"\nYou have matched: {number_of_matches} and Mega-Ball!" if lottery_megaball == usr_mega else f"\nYou've matched: {number_of_matches}")
    print(f"Matches: {hits}" if number_of_matches else print("No match"))
    print(msg, "\nYou have won {}".format(prize) if prize > 0 else "\nThank you for playing! We wish you good luck next time!")


def main():
    message = """
1: Start game.
2: List prizes info:
3: How to Play info
x: Exit or End Game.
$->: """
    flag = True
    while flag:
        try:
            selection = input(message)
            match selection:
                case "1":start_game()
                case "2":display_prize_info()
                case "3":display_howto()
                case "x":
                    break
                case _:
                    raise ValueError("Invalid input. 1, 2 or x are the only valid options.")
        except TypeError as type_err:
            print(f"TypeError: {type_err}")
            print(f"Ending game...")
            flag = False
        except ValueError as val_err:
            print(f"ValueError: {val_err}")
            print(f"Ending game...")
            flag = False
    print("Thank you for playing with New York Lottery!")
if __name__ == "__main__":
    main()