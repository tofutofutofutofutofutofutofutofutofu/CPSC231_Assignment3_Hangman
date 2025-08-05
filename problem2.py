# Christopher Lee
# ID: 10136117
import random
import string
import sys

# You can replace sys.argv[1] with the file name if you want to test here
lexiconFile = sys.argv[1]
letterList = []
blanks = []
guessedList = []
badGuessedList = []
word = ""
guessesLeft = 8
lettersGuessed = 0

# Here we open the file and store it as a string
theFile = open(lexiconFile, 'r')
stringLexicon = theFile.read()
theFile.close()

# Turn the string into a list and then delete the extra empty entry
listLexicon = stringLexicon.split("\n")
if '' in listLexicon:
    listLexicon.remove('')

# This is to reroll random words until we get a word that's 4 letters or longer
while len(word) < 2:
    word = listLexicon[random.randint(0, len(listLexicon) - 1)]
    word.lower()

# Create a List that's just blanks but the length is equal to the word
for letter in word:
    blanks.append("_")

# Optional line because I'm bad at hangman
# print(word)

# Win condition is stored in while
while guessesLeft != 0 and lettersGuessed != len(word):
    print(f"The secret word looks like: {' '.join(blanks)}")
    print(f"You have {guessesLeft} guesses remaining.")

    # Uses a list to store and display bad guesses
    if len(badGuessedList) > 0:
        badGuessedList.sort()
        print(f"Your bad guesses so far: {' '.join(badGuessedList)}")

    # User input for the letter guess
    currentGuess = input("What's your next guess?")
    currentGuess = currentGuess.lower()

# Conditions that I want to be met by the guesses

    # You can guess the whole word at once if you want
    # Technically can cheat using this but whatever
    if currentGuess == word:
        lettersGuessed = len(word)
        print("\nNice guess! Congratulations!\n")
    # Blank Guess
    elif currentGuess == "" or currentGuess == " ":
        print("\nYou didn't guess! Please try again.\n")
    # Long Guess
    elif len(currentGuess) >= 2:
        print("\nYour guess is too long, please try again.\n")
    # Checking for numbers
    elif any(letter.isdigit() for letter in currentGuess):
        print("\nPlease guess letters, not numbers.\n")
    # Check for symbols
    elif any(letter in set(string.punctuation) for letter in currentGuess):
        print("\nPlease guess letters, not symbols.\n")
    # Check for guessed letters
    elif currentGuess in guessedList:
        print(f"\nYou've already guessed \"{currentGuess}\"! Guess a different letter!\n")

    # If the letter isn't in the word go here, increments lose counter and adds to bad guess list
    elif currentGuess not in word:
        print(f"\nSorry, there is no \"{currentGuess}\"\n")
        guessesLeft -= 1
        guessedList.append(currentGuess)
        badGuessedList.append(currentGuess)

    # If every thing else is fine we go here
    else:
        # This replaces the blanks with the letters from the word list and increments the win total
        for index, wordletter in enumerate(word):
            if currentGuess == wordletter:
                blanks[index] = wordletter
                lettersGuessed += 1
                guessedList.append(currentGuess)
        if lettersGuessed != len(word):
            print("\nNice guess!\n")
        else:
            # Extra message in the case the word has been fully guessed
            print("\nNice guess! Congratulations!\n")
# Lose case
if guessesLeft == 0:
    print(" _________     ")
    print("|         |    ")
    print("|         0    ")
    print("|        /|\\  ")
    print("|        / \\  ")
    print("|              ")
    print("|              ")
    print("You ran out of guesses...")
    print(f"The word was {word}")
# Win case
elif lettersGuessed == len(word):
    print(f"You guessed the secret word: {word}")

input("Press the enter key to quit.")
