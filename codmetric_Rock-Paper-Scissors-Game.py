import random

def play_game():
    """Main game function"""
    print("Welcome to Rock-Paper-Scissors!")
    print("Rules: Rock beats scissors, scissors beat paper, paper beats rock.")
    
    # Game setup
    choices = ['rock', 'paper', 'scissors']
    valid_inputs = {'r', 'p', 's', 'rock', 'paper', 'scissors'}
    short_to_long = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    
    while True:
        # Get user input
        user_choice = input("\nChoose (R)ock, (P)aper, (S)cissors or (Q)uit: ").lower()
        
        # Check for quit
        if user_choice == 'q':
            print("Thanks for playing! Goodbye.")
            break
        
        # Validate input
        if user_choice not in valid_inputs:
            print("Invalid choice. Please try again.")
            continue
        
        # Convert short forms to full words
        if len(user_choice) == 1:
            user_choice = short_to_long[user_choice]
        
        # Computer makes random choice
        computer_choice = random.choice(choices)
        
        # Display choices
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Determine winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'scissors' and computer_choice == 'paper') or
            (user_choice == 'paper' and computer_choice == 'rock')
        ):
            print("You win!")
        else:
            print("Computer wins!")

if __name__ == "__main__":
    play_game()
