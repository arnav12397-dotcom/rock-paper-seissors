def get_player_choice():
    while True:
        choice = input("Enter your choice:")
        choice = choice.lower()
        if choice in ["rock","paper","scissors"]:

            return choice
        else:
            print("Invalid input! Please enter rock, paper, or scissors.")

