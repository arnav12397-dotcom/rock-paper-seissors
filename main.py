from sympy.codegen.ast import continue_

from player import get_player_choice
from computer import get_computer_choice
from logic import decide_winner
from score import update_score, display_score
from utile import play_again


def main():
    print("☆*: .｡. o(≧▽≦)o .｡.:*☆")
    print("Welcome to Rock Paper Scissors")


    while True:
        computer = get_computer_choice()
        player = get_player_choice()


        print(f"\nYou chose: {player}")
        print(f"Computer chose: {computer}")

        result = decide_winner(player, computer)
        print(result)

        update_score(result)
        display_score()

        if not play_again():
             print("Thanks for playing")
             break


if __name__ == "__main__":
    main()