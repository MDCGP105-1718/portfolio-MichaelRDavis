import random
import os
import string

FILENAME = "words.txt"
DEBUG = 0

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
tries = 0
maxTries = 6

# Get the word size
wordSize = len(wordToGuess)

# Introduce the user to the game of hangman
print("Welcome to Hangman!\n")
print("Insert a letter to guess too many wrong guesses and you'll be hanged!\n")
print(f"The word I'm thinking of is {wordSize} letters long\n")

# Ask the use to insert a word to guess
while tries <= maxTries:
    guessLetter = input("Insert a letter to guess:\n")
    # Check to see if word guessed is in list of words
    for i in wordToGuess:
        print(i)
    if i in guessLetter:
        print("You guessed correctly well done human!\n")
    else:
        print("Guess Again!")
        print(f"You have {tries} remaining!\n")
        tries += 1
    if(tries >= 5):
        print("You have been hanged!")
        break
