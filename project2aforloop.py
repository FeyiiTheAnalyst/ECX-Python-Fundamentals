# Olorode Feyisayomi
secret_number = 32 
attempt = 5 #No of attempts
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100."
f"\nYou have {attempt} attempts to guess it.")

# Game Loop
for attempt in range (attempt, 0 , - 1 ):  #starts at the initial no of attempts which is 5
  # stops at 0 at an interval of -1
     user_number = int(input("Enter your guess:") ) # allows an input inform of integer  
     if user_number == secret_number:
       print("Congratulations! You've guessed the number!") #prints congratulations if the secret_no is guessed right
       break; # Stops the program once the Condition is satisfied
     if user_number > secret_number:
       print(f"Too High!\nYou have {attempt -1} attempts left")
     #prints too high with the number of attempts left when secret_number is > user number
     else:
       print(f"Too Low!\nYou have {attempt -1} attempts left")
else:
    print("Game Over! The number was 32.")  #once the rage of the for loop gets to zero
    #it returns game over and ends the game.
        
             
    