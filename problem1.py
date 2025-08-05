# Christopher Lee
# ID: 10136117
import sys

endings = {1: 'st', 2: 'nd', 3: 'rd'}

# ??? was this the real assignment this was pretty tricky
def ordinal(number):
    # if the end of the number is between 10 and 20 > use th
    if 10 <= number % 100 <= 20:
        numberending = 'th'
    # otherwise look up the ending for the last number in the number, and add th for non 1-3
    else:
        numberending = endings.get(number % 10, 'th')
    return str(number) + numberending


# Take in command line arguments
lexiconFile = sys.argv[1]
wordLook = sys.argv[2]
letterList = []
# Making it not case sensitive, check for I
if wordLook == "i":
    wordLook = wordLook.upper()
else:
    wordLook = wordLook.lower()

# open and taking the values from the lexicon
theFile = open(lexiconFile, 'r')
stringLexicon = theFile.read()
theFile.close()

# creating a list from the lexicon
listLexicon = stringLexicon.split("\n")

# remove the extra empty entry if necessary
if '' in listLexicon:
    listLexicon.remove('')

# Simple way to search if string is in list
if wordLook in listLexicon:
    print(f'According to our lexicon, "{wordLook}" is the '
          # Add one because it's using index which starts from 0
          f'{ordinal(listLexicon.index(wordLook) + 1)} most common word in contemporary American English.')

else:
    print(f"According to our lexicon, \"{wordLook}\" is not in the 4000 most common words of contemporary American English.")

# Each letter in the word gets added to the list if it's not already in the list
for letter in wordLook:
    if letter not in letterList:
        letterList.append(letter)
# This sorts it alphabetically, gets kinda weird with symbols and numbers
letterList.sort()
print(f'It contains the following letters: {" ".join(letterList)}')
