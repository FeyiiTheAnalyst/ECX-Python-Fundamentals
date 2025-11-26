
secret_number = 32  
# Initialize variables
attempts_left = 5
has_won = False
# Print welcome message
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
print(f"You have {attempts_left} attempts to guess it.")


while attempts_left>0 or has_won  :
    # TODO: Get the player's guess
    guess = int(input("Enter the number:"))  # Add code to get and convert player's input

    # TODO: Decrease the number of attempts left
    attempts_left -= 1

    ''' TODO: Add if/elif/else statements to:
     1. Check if the guess is correct (equals secret_number)
     2. Check if the guess is too high
     3. Check if the guess is too low
     Print appropriate messages for each case'''
    if guess == secret_number:      
  # guess is correct
       print("Congratulations! You've guessed the number!")
       break
    if guess > secret_number:  # guess is too high
        print("Too high!")
    else: #guess < secret_number:
        print("Too Low!")# guess is too low
    print(f"You have {attempts_left} attempts left.")

    ''' TODO: Add code to handle end of game
    If player ran out of attempts, print "Game Over" message
    Don't forget to tell them what the number was!'''
else :#attempts_left == 0 or has_won:
    print("Game Over! The number was 32.")
     
