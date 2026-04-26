def decide_winner(player, computer):
    if player == computer:
        return "It's a tie!"

    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You win!"

    else:
        return "Computer wins!"
