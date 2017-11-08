import string
import random

FILENAME = "lyrics1.txt"
DEBUG = 1

# Dictionary of words found
wordFrequency = {}

# Read the file, open up file in memory and read words from file
def findWords():
    fileObj = open(FILENAME)
    for words in iter(fileObj):
        if DEBUG:
            print(" ", len(words), "words loaded.")
    return words

findWords()
