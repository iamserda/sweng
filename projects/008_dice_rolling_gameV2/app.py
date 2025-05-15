import random

MAX_SCORE = 21


class Player:
    def __init__(self, name):
        self.name = name
        self.roll_history = []
        self.score = 0
        self.roll_count = 0

    def roll_dice(self):
        dice1, dice2 = random.randrange(1, 6), random.randrange(1, 7)
        self.roll_count += 1
        self.score += dice1 + dice2
        self.roll_history.append([dice1, dice2])


def show_menu():
    menu = (
        "\n1. Single-Player Mode\n2. Two-Player Mode 3. Play\n9. Forfeit",
        "x. End the game\n",
    )
    selection = input("Enter your selection from the menu:")
    if selection.isalpha:
        selection = 0
    return int(selection)


def start_game():

    p1_name = input("Enter your name: ")
    player1 = Player(p1_name)
    p2_name = input("Enter your name: ")
    player2 = Player(name=p2_name)
    player1_turn = True

    while player1.score < 21 or player2.score < 21:
        player1.roll_dice()
        print(
            f"\nname: {player1.name} -> rolled: {player1.roll_history[-1]} -> score: {player1.score}"
        )
        player2.roll_dice()
        print(
            f"name: {player2.name} -> rolled: {player2.roll_history[-1]} -> score: {player2.score}"
        )

        if player1.score > 21:
            print(f"{player2.name} wins!")

        if player2.score > 21:
            print(f"{player1.name} wins!")

    print("\nThanks for playing!\nEnding Game!")


if __name__ == "__main__":
    start_game()
