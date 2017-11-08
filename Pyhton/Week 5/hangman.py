import random
import os
import string

FILENAME = "words.txt"
DEBUG = False

# Read & open the file into memory
def readFile():
    fileObject = open(FILENAME)
    return fileObject

# Get the size of the text file
def getFileSize(fileObject):
    fileSize = os.stat(fileObject).st_size
    return fileSize

# Get the word list from the text file
def getWordList(fileObject):
    fileObject = open(FILENAME)
    strObj = fileObject.readline()
    wordList = strObj.split()
    print(" ", len(wordList), "words loaded.")
    return wordList

# Get a random string from a word list
def getRandomString(wordList):
    return random.choice(wordList)

# The list of words for the user to guess
tempFileObj = readFile()
wordToGuess = getRandomString(getWordList(tempFileObj))

# Print wordToGuess for debugging purposes
if DEBUG:
    print(f"{wordToGuess}")

# The max number of tries
tries = 6

# Get the word size
wordSize = len(wordToGuess)

clue = wordSize * ["_"]
lettersGuessed = ""
guesses = 0
lettersRight = 0
lettersWrong = 0

# Introduce the user to the game of hangman
print("Welcome to Hangman!\n")
print("Insert a letter to guess too many wrong guesses and you'll be hanged!\n")
print(f"The word I'm thinking of is {wordSize} letters long\n")

# Ask the use to insert a word to guess
while lettersWrong != tries and ("".join(clue) != wordToGuess):
    guessLetter = input("Insert a letter to guess:\n")
    letter = guessLetter

    if len(letter) == 1 and letter.isalpha():
        if lettersGuessed.find(letter) != -1:
            print(f"You already guessed the letter {letter} please guess another\n")
        else:
            lettersGuessed += letter
            firstIndex = wordToGuess.find(letter)
            if firstIndex == -1:
                lettersWrong += 1
                print("You guessed wrong!\n")
            else:
                print(f"You guessed correctly the letter {letter} is a letter in the word!\n")
                for i in range(wordSize):
                    if letter == wordToGuess[i]:
                        clue[i] = letter
    else:
        print("Please guess again!\n")

    print(" ".join(clue))
    print("Guesses: ", lettersGuessed)

    if lettersWrong == tries:
        print("Sorry you ran out of guesses.\n")
        print(f"The word was {wordToGuess}.\n")
        break
    if "".join(clue) == wordToGuess:
        print("Congratulations, you won!")
        print(f"The word was {wordToGuess}.\n")
        break
