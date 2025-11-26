#Student Name: Olorode Feyisayomi
# Import the random module to use for generating random values
import random

# Read the file content into a variable
with open("words.txt", mode="r", encoding="ISO-8859-1") as file:
    content = file.read()

# Split the content of the file into a list of words, assuming words are separated by ", "
word_list = content.split(", ")

# Function to check if a word is a palindrome
# A palindrome is a word that reads the same forward and backward
def is_palindrome(word):
    return word == word[::-1]  # :: responsible for reversing words,-1 starts from the last letter and returns the word

# Function to generate anagrams for a list of words
# An anagram is a rearrangement of letters to form a different word
def generate_anagrams(words):
    anagram_groups = {}  #Empty Dictionary to group words with the same letters
    for word in words:
        key = tuple(sorted(word))  # Sort the letters in the word and use as a key
        anagram_groups.setdefault(key, []).append(word)  
        '''
        setdefault checks if the key ( sorted letters of the word) already exists in the dictionary.
        If the key exists, it returns the associated value (a list of words).
        If the key does not exist, 
        it creates a new entry in the dictionary with the key and initializes its value as an empty list ([]).
        Then, the current word is appended to the list corresponding to the key.
         '''
    anagram_list = []  # List to store all anagram groups
    for group in anagram_groups.values():
        if len(group) > 1:  # Only include groups with more than one word
            anagram_list.extend(group)  # Add the anagrams to the list
    return anagram_list

# Main function for the word game
def word_game():
    print("Welcome to the word game\nType 'info' for instructions or 'end' to quit.")
    
    # Start a loop to keep the game running until the user decides to quit
    while True:
        user_input = input("Enter a Word/command:").lower()  # Take input from the user and convert to lowercase

        if user_input == "info":
            # Display instructions for the game
            print("""This game allows you to play with a list of words in the following ways:
                    1. 'summarize' - Get statistics about palindromes, anagrams, unique, and duplicate words.
                    2. 'example' - See examples of palindromes and anagrams.
                    3. 'length' - Enter a word length to find how many words match it.
                    4. 'consonant' - Get 10 random words starting and ending with consonants.
                    5. 'info' - Display this help message.
                    6. 'end' - Quit the game.
                    7. Enter any other word to check if it's in the list."""
                )  
      
        elif user_input == "summarize":
             # Calculate and display statistics about the word list
             palindrome = [word for word in word_list if is_palindrome(word)]  # List of palindromes
             unique_word = set(word_list)  # Unique words (no duplicates)
             duplicate_words = [word for word in word_list if word_list.count(word) > 1]  # Duplicates
             anagrams = generate_anagrams(word_list)  # Find all anagrams
             summary = {
                "palindromes": len(palindrome),
                "anagrams": len(anagrams),
                "unique_words": len(unique_word),
                "duplicate_words": len(set(duplicate_words))
                }
             print("Summary:", summary) 
        
        elif user_input == "example":
             # Display examples of palindromes and anagrams
             palindrome = [word for word in word_list if is_palindrome(word)]
             random_palindromes = random.sample(palindrome, min(5, len(palindrome)))  # Get up to 5 random palindromes
             anagrams = generate_anagrams(word_list)  # Get all anagrams
             random_anagrams = random.sample(anagrams, min(4, len(anagrams)))  # Get up to 4 random anagrams
             example = {
             "palindromes": random_palindromes,
             "anagrams": tuple(random_anagrams),#converts the list to a tuple
             }
             print("Example:", example)

        elif user_input == "length":
            # Find words of a specific length
            try:
               length = int(input("Enter the desired word length: "))  # Convert input to an integer
               count = sum(1 for word in word_list if len(word) == length)  # Count words with the given length
               print(f"Number of words with length {length}: {count}")
            except ValueError:
                print("Invalid input. Please enter a valid number.")  # Handle invalid inputs
        
        elif user_input == "consonant":
            # Find and display words that start and end with consonants
            consonants = "bcdfghjklmnpqrstvwxyz"  # Define consonants
            consonant_words = [
                word for word in word_list
                if word[0].lower() in consonants and word[-1].lower() in consonants
            ]  # checks for word that starts and end with consonants after converting to lower case
            random_words = random.sample(consonant_words, min(10, len(consonant_words)))  # Get up to 10 random words
            print("Random words that start and end with consonants:")
            for word in random_words:
                print(word.lower())  # Print each word on a new line
        
        elif user_input == "end":
            # End the game
            print("Thank you for playing! Goodbye!")
            break
        
        else:
            # Check if the word is in the list
            if user_input in word_list:
              print(f"The word '{user_input}' is in the list.")
            else:
               print(f"The word '{user_input}' is NOT in the list.")

  # initialize the game
word_game()