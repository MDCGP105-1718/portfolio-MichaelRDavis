import string
import random
import collections

FILENAME = "lyrics1.txt"
DEBUG = False

# Read the file, open up file in memory and read words from file
def findWords():
    fileObj = open(FILENAME)
    for words in iter(fileObj):
        words = fileObj.read()
        if DEBUG:
            print(" ", len(words), "words loaded.")
    wordList = list(words.split())
    return wordList

# Count the number of words in file, ask the user to insert a counter
def countNumWords(wordList):
    x = int(input("Insert a number to search for the most common words\n"))
    numWords = collections.Counter(wordList)
    print(numWords.most_common(x))

countNumWords(findWords())
