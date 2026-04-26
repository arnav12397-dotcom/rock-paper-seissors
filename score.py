player_score = 0
computer_score = 0
def update_score(result):
    global player_score, computer_score

    if result == "You win!":
        player_score += 1
    elif result == "Computer wins!":
        computer_score += 1

def display_score():
    print(f"player score {player_score} // Computer score: {computer_score}")
