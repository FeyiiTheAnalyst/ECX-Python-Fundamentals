#Student Name:Olorode Feyisayomi
import requests
'''user enters a word they want to search for ,converts it to lowercase,checks the status code of the API 
and prints out the appropriate result'''
def search_dictionary():
    while True:
        word = input("Hello! Enter a word to search (or type 'exit' to quit):").strip()

        if word.lower() == "exit":
            print("Goodbye! Thanks for using the dictionary")
            break
        response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

        if response.status_code == 404:
            print(f"Sorry. The word '{word}' isn't in the dictionary.")
            continue
        if response.status_code != 200:
            print("Something went wrong with the API. Please try again later.")
            continue
        '''checks if etymology choice is available,iterates through meanings to check for parts of speech,
        then adds evrything found'''
        data = response.json()
        try:
            etymology_choice =int(input(f"There are {len(data)} etymology available .Select from 1 -{len(data)}:"))
            if etymology_choice < 1 or etymology_choice > len(data):
                print("Invalid Selection.Try again")
                continue
           
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        selected_etymology =data[etymology_choice - 1]
        meanings = selected_etymology.get("meanings",[])
        if not meanings:
            print("No meanings found for this etymology.")
            continue
        parts_of_speech = [meaning["partOfSpeech"] for meaning in meanings]
        parts_of_speech.append("all")
        parts_of_speech = list(set(parts_of_speech))
        print(f"{len(parts_of_speech) - 1} part(s) of speech found.")

        pos_choice = input(f"Select part of speech {parts_of_speech}: ").strip().lower()

        if pos_choice not in parts_of_speech:
            print("Invalid part of speech. Try again.")
            continue

        if pos_choice == "all":
            available_meanings = meanings
        else:
            available_meanings = [m for m in meanings if m["partOfSpeech"].lower() == pos_choice]

        if not available_meanings:
            print(f"No definitions found for part of speech '{pos_choice}'.")
            continue

        for meaning in available_meanings:
            print(f"Part of Speech: {meaning['partOfSpeech']}")
            for idx, definition in enumerate(meaning["definitions"], start=1):
                print(f"Definition {idx}: {definition['definition']}")
                if "example" in definition:
                    print(f"Example Usage: {definition['example']}")

        if selected_etymology.get("phonetics"):
            for phonetic in selected_etymology["phonetics"]:
                if phonetic.get("audio"):
                    print(f"You can listen here: {phonetic['audio']}")



if __name__ == "__main__":
    search_dictionary()
