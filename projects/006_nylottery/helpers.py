from random import randint


def greeting(user_name=None):
    greet = (
        "\nHi {}! Welcome to the New York Lottery!".format(user_name)
        if user_name
        else "Welcome to the New York Lottery!\n"
    )
    print(greet)


def display_howto():
    message = """\nHere is how to play:
1. Choose five (5) numbers from 1-70 as your Five-Picks.
2. Choose one (1) number from 1-25 as your Mega-Ball.
\n\nHow to win the Mega Millions jackpot?
- Match the Five-Picks numbers and the Mega Ball on your ticket.
- Winning draw game tickets expire one (1) year from the date of the draw."""
    print(message)


def display_prize_info():
    message = """Winning Prizes List: - Jackpot: Match 5 + Powerball: You win the Mega Jackpot.\n- Second: Match 5: You win a cool $1,000,000 USD.\n- Third: Match 4 + Powerball: You win $10,000 USD.\n- Fourth: Match 4: You win the $500.\n- Fifth: Match 3 + Powerball: You win $200.\n- Sixth: Match 3: You win $10.\n- Seventh: Match 2 + Powerball: You win $10.\n- Eighth: Match 1 + Powerball: You win $4.\n- Ninth: Match Powerball ONLY: You win $2."""

    print(message)


def get_user_selection():
    """Get user's lottery input. Five (5) numbers between 1 and 70, and a sixth number as the mega-ball number (1-25)"""
    message = (
        "Please enter six (6) numbers for the lottery separated by a comma (,):\n$: "
    )
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
    return five_picks, mega_ball


def print_user_selection(user_five, user_mega):
    print(f"You have selected:\nFive-Pick: {user_five}\nMega Ball{user_mega}.")


def generate_lottery_five():
    """returns a set of five numbers as the winning lottery numbers."""
    five_pick_set = set([randint(1, 70) for i in range(5)])
    while len(five_pick_set) < 5:
        five_pick_set.add(randint(1, 70))
    return five_pick_set


def generate_mega_ball():
    return randint(1, 25)


def verify_picks(lottery, user_picks):
    answer = lottery.intersection(user_picks)
    return answer


def announce_lottery(lottery_five, lottery_megaball):
    print("\nGenerating NY Lottery:")
    print("5-Pick:", lottery_five)
    print("Mega-Ball:", lottery_megaball)
    print()


def get_prize(matched: int, mega_ball=False):
    """
    Determines the prize and message based on the number of matched numbers
    and whether the Mega Ball (Power Ball) is matched.

    Args:
        matched (int): The number of matched numbers (0 to 5).
        mega_ball (bool, optional): Indicates if the Mega Ball is matched. Defaults to False.

    Returns:
        tuple: A tuple containing:
            - message (str): A message describing the result of the lottery draw.
            - prize (int): The prize amount in dollars. Returns 0 if no prize is won.

    Notes:
        - Matching 0 to 5 numbers without the Mega Ball results in different prize tiers.
        - Matching the Mega Ball increases the prize tier or awards a prize even with no matched numbers.
        - Matching all 5 numbers and the Mega Ball results in the jackpot.
    """
    prizes = {
        "jackpot": 310000000,
        "second": 1000000,
        "third": 10000,
        "fourth": 500,
        "fifth": 200,
        "sixth": 10,
        "seventh": 10,
        "eighth": 4,
        "ninth": 2,
    }
    prize = 0
    match (matched):
        case 0:
            message = "You did not win a prize this time, better luck next time! Thank you for playing."
            if mega_ball:
                message = "Congratulations! You've matched the Powerball!"
                prize = prizes["ninth"]
        case 1:
            message = "Yay, you've matched 1 Number!"
            if mega_ball:
                prize = prizes["eighth"]
        case 2:
            message = "Nice, you've matched 2 numbers this week!"
            if mega_ball:
                prize = prizes["seventh"]
        case 3:
            message = "Awesome, you've matched 3 numbers!"
            prize = prizes["sixth"]
            if mega_ball:
                prize = prizes["fifth"]
        case 4:
            message = "Amazing, you've matched 4 numbers!"
            prize = prizes["fourth"]
            if mega_ball:
                prize = prizes["third"]
        case 5:
            message = "Incredible! Wow, you've matched 5 numbers!"
            prize = prizes["second"]
            if mega_ball:
                message += " + POWER BALL! Jackpot! Jackpot! Jackpot! Jackpot! Jackpot! Jackpot!"
                prize = prizes["jackpot"]
        case _:
            message = "You did not win a prize this time, better luck next time! Thank you for playing."

    if mega_ball:
        message += " And you have matched the Power Ball!"
    return message, prize


def get_user_name():
    user_name = input("Enter your name: ")
    return user_name
