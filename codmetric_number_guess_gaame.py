import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = input("\nEnter your guess (1-100) or 'quit' to exit: ")
            
            if guess.lower() == 'quit':
                print(f"\nGame ended. The secret number was {secret_number}.")
                break
            
            guess = int(guess)
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"\nCongratulations! You guessed the number in {attempts} attempts!")
                break
                
        except ValueError:
            print("Invalid input. Please enter a number or 'quit'.")

if __name__ == "__main__":
    number_guessing_game()
