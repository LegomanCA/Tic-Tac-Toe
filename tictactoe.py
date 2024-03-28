import random

def get_user_choice():
    while True:
        print("Choose one:")
        print("1) Rock")
        print("2) Paper")
        print("3) Scissors")
        choice = input("Enter your choice (1/2/3): ")
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'draw'
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        return 'user'
    else:
        return 'computer'

def main():
    user_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("Your choice:", user_choice)
        print("Computer's choice:", computer_choice)

        winner = determine_winner(user_choice, computer_choice)
        if winner == 'user':
            user_score += 1
            print("You win!")
        elif winner == 'computer':
            print("Computer wins!")
            break
        else:
            print("It's a draw!")

        print("Your score:", user_score)
        print()

if __name__ == "__main__":
    main()
