from random import randint
def get_user_name():
    user_name = input("Enter your name: ")
    return user_name

def greeting(user_name=None):
    greet = "\nHi {}! Welcome to the New York Lottery!".format(user_name) if user_name else "Welcome to the New York Lottery!\n"
    print(greet)

def print_howtoplay(user_name=None):
    message = """
Here is how to play:
- Choose five (5) numbers from 1 to 70.
- Then choose one (1) number from 1 to 25 for your Mega Ball.

How to win the Mega Millions jackpot? 
- Match the five-pick numbers and the Mega Ball on your ticket.
- Winning draw game tickets expire one (1) year from the date of the draw."""
    print(message)

def print_prizes_info():
    message = """
Match 5 + Powerball: You win the Mega Jackpot.
Match 5: You win a cool $1,000,000 USD.
Match 4 + Powerball: You win $10,000 USD.
Match 4: You win the $500.
Match 3 + Powerball: You win $200.
Match 3: You win $10.
Match 2 + Powerball: You win $10.
Match 1 + Powerball: You win $4.
Match Powerball: You win $2."""

    print(message)

def get_user_selection():
    """Get user's lottery input. Five (5) numbers between 1 and 70, and a sixth number as the mega-ball number (1-25)"""
    message = "Please enter six (6) numbers for the lottery separated by a comma (,):\n$: "
    five_picks = set()
    mega_ball = 0

    while not len(five_picks) == 5 or not 1 <= mega_ball <= 25:
        user_input = input(message)
        user_selection = [int(elem.strip()) for elem in user_input.split(",")]
        if len(user_selection) != 6:
            continue
        five_picks = set(user_selection[:5])
        mega_ball = user_selection[5]
        if min(five_picks) < 1 or max(five_picks) > 70:
            five_picks = set()
            mega_ball = 0
            continue
    print("\nYour Five-Picks: {}".format(five_picks))
    print("\nYour Mega-Ball: {}".format(mega_ball))
    return five_picks, mega_ball


def print_user_selection(user_five, user_mega):
    print(f"You have selected:\nFive-Pick: {user_five}\nMega Ball{user_mega}.")


def generate_lottery_five():
    five_pick_set = set()
    while len(five_pick_set) < 5:
        five_pick_set = set([randint(1, 70) for i in range(5)])
    return five_pick_set


def generate_mega_ball():
    return randint(1, 25)

def verify_picks(lottery, user_picks):
    answer = lottery.intersection(user_picks)
    print(answer)
    return answer




def announce_lottery(lottery_five, lottery_megaball):
    print("Generating Lotter:")
    print("Lottery 5-Pick:", lottery_five)
    print("Lottery Mega-Ball:", lottery_megaball)
    


def get_prize(matched:int,power_ball=False):
    print(matched, power_ball)
    prizes = {
        "jackpot": 310000000,
        "second": 1000000,
        "third": 10000,
        "fourth":500,
        "fifth":200,
        "sixth": 10,
        "seventh": 10,
        "eighth": 4,
        "ninth": 2
    }
    prize = 0
    match(matched):
        case 0:
            if power_ball:
                message = "Congratulations! You've matched the Powerball!"
                prize = prizes["ninth"]
        case 1:
            message = "Yay, you've matched 1 Number!"
            if power_ball:
                prize = prizes["eighth"]
        case 2:
            message = "Nice, you've matched 2 numbers this week!"
            if power_ball:
                prize = prizes["seventh"]
        case 3:
            message = "Awesome, you've matched 3 numbers!"
            prize = prizes["sixth"]
            if power_ball:
                prize = prizes["fifth"]
        case 4:
            message = "Amazing, you've matched 4 numbers!"
            prize = prizes["fourth"]
            if power_ball:
                prize = prizes["third"]
        case 5:
            message = "Incredible! Wow, you've matched 5 numbers!"
            prize = prizes["second"]
            if power_ball:
                message += " + POWER BALL! Jackpot! Jackpot! Jackpot! Jackpot! Jackpot! Jackpot!"
                prize = prizes["jackpot"]
        case _:
            message = "You did not win a prize this time, better luck next time! Thank you for playing."

    if power_ball:
            message += " And you have matched the Power Ball!"
    return message, prize


def start_game():
    username = get_user_name()
    greeting(username)

    user_five, usr_mega = get_user_selection()
    lottery_five = set([32, 1, 43, 20, 21]) #generate_lottery_five()
    lottery_megaball = 23 # generate_mega_ball()
    announce_lottery(lottery_five, lottery_megaball)
    
    hits = verify_picks(lottery_five, user_five)
    msg, prize = get_prize(len(hits), True if lottery_megaball == usr_mega else False)
    print(f"You have matched: {hits}")
    print(msg, "You have won {}".format(prize) if prize > 0 else "\nThank you for playing! We wish you good luck next time!")


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
                case "2":print_prizes_info()
                case "3":print_howtoplay()
                case "x":
                    break
                case _:
                    raise ValueError("Invalid input. 1, 2 or x are the only valid options.")
        except TypeError as type_err:
            print(f"TypeError: {type_err}")
            print(f"Ending game...")
            flag = False
        except ValueError as val_err:
            print(f"TypeError: {val_err}")
            print(f"Ending game...")
            flag = False
    print("Thank you for playing with New York Lottery!")
if __name__ == "__main__":
    main()