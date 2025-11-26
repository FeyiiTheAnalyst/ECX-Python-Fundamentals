#Student Name:Olorode Feyisayomi
# Import the required Library
import random

# Select a random word and welcome your user
words = ["cat", "children", "money", "computer", "school", "python", "program", "coding", "farida", "tomiwa", "ecx"]
selected_word = random.choice(words)
print("Welcome to the Hangman game!!")

# Create a list representation of the selected word for easier manipulation
word_as_list = ["_" for letter in selected_word]
print("You have to guess this word: " + "".join(word_as_list))

# Set game properties
end_of_game = False
life = 6
guessed_letters = []  # Keep track of guessed letters

# Start game
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check if the letter was guessed already
    if guess in guessed_letters:
        print("You've already guessed that letter. Try again.")
        continue
    guessed_letters.append(guess)  # Add the guessed letter to the list

    # Check if they made a correct guess
    if guess in selected_word:
        # Loop through each letter in the selected word and its index
      for index, letter in enumerate(selected_word):
    # Check if the current letter matches the user's guessed letter
          if letter == guess:
        # If the letter matches, update the word_as_list at the corresponding index with the guessed letter
            word_as_list[index] = guess
            print("Congrats, that's correct!")
    else:
        print("That's not in the word. Try again!")
        life -= 1
        print(f"You have {life} lives left.")
    
    # Display the current state of the guessed word
    print("Current word:", "".join(word_as_list))

    # Check if they've completed the word
    if "_" not in word_as_list:
        end_of_game = True
        print("You win!")
    
    # Check if they have lost
    if life == 0:
        end_of_game = True
        print("Sorry, you lose!")
        print(f"The word was: {selected_word}.")
