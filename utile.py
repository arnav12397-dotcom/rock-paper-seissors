def play_again():
    while True:
        choice = input("Do you want to play again? (yes/no): ").lower()

        if choice == "yes":
            return True
        elif choice == "no":
            return False
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")
