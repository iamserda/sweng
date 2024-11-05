import random

player1 = []
player2 = []
player1_turn = True
max_score = 21

while sum(player1) < 21 or sum(player2) < 21:
    new_score = random.randrange(1,6)
    if player1_turn:
        player1.append(new_score)
        p1_score = sum(player1)
        if p1_score == 21:
            print("Player 1 wins!")
            break
        if p1_score > 21:
            print("Player 2 wins!")
            break
    else:
        player2.append(new_score)
        p2_score = sum(player2)
        if p2_score == 21:
            print("Player 2 wins!")
            break
        if p2_score > 21:
            print("Player 1 wins!")
            break
    player1_turn = not player1_turn
    
print(f"Player1: {p1_score} Player2: {p2_score}")
