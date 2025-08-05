import random
import string
import sys

lexiconFile = "whosthat.txt"
letterList = []
blanks = []
guessedList = []
badGuessedList = []
word = ""
guessesLeft = 8
lettersGuessed = 0
theFile = open(lexiconFile, 'r')
stringLexicon = theFile.read()
theFile.close()

listLexicon = stringLexicon.split("\n")
if '' in listLexicon:
    listLexicon.remove('')

while len(word) < 2:
    word = listLexicon[random.randint(0, len(listLexicon) - 1)]

for letter in word:
    blanks.append("_")
print(blanks)

while guessesLeft != 0 and lettersGuessed != len(word):
    print(f"The secret word looks like: {' '.join(blanks)}")
    print(f"You have {guessesLeft} guesses remaining.")

    if len(badGuessedList) > 0:
        badGuessedList.sort()
        print(f"Your bad guesses so far: {' '.join(badGuessedList)}")
    currentGuess = input("What's your next guess?")
    currentGuess = currentGuess.lower()
    if currentGuess == word:
        lettersGuessed = len(word)
        print("\nNice guess! Congratulations!\n")
    elif currentGuess == "" or currentGuess == " ":
        print("\nYou didn't guess! Please try again.\n")
    elif len(currentGuess) >= 2:
        print("\nYour guess is too long, please try again.\n")
    elif any(letter.isdigit() for letter in currentGuess):
        print("\nPlease guess letters, not numbers.\n")
    elif any(letter in set(string.punctuation) for letter in currentGuess):
        print("\nPlease guess letters, not symbols.\n")
    elif currentGuess in guessedList:
        print(f"\nYou've already guessed \"{currentGuess}\"! Guess a different letter!\n")
    elif currentGuess not in word:
        print(f"\nSorry, there is no \"{currentGuess}\"\n")
        guessesLeft -= 1
        guessedList.append(currentGuess)
        badGuessedList.append(currentGuess)
    else:
        for index, wordletter in enumerate(word):
            if currentGuess == wordletter:
                blanks[index] = wordletter
                lettersGuessed += 1
                guessedList.append(currentGuess)
        if lettersGuessed != len(word):
            print("\nNice guess!\n")
        else:
            print("\nNice guess! Congratulations!\n")

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
elif lettersGuessed == len(word):
    print(f"You guessed the secret word: {word}")

input("Press the enter key to quit.")
