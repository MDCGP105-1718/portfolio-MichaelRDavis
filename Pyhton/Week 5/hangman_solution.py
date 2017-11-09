# Copyright Chris Janes 2017. All Rights Reserved.
# Author Chris Janes - 9 November 2017

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    correct = 0
    for letter in secret_word:
        if letter in letters_guessed:
            correct += 1

    return correct == len(secret_word)



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    ret = ''

    for letter in secret_word:
        if letter in letters_guessed:
            ret += letter + ' '
        else:
            ret += '_ '

    return ret



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    ret = ''

    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            ret += letter

    return ret

def in_secret_word(secret_word, guess):
    return guess in secret_word

def print_output(message, guessed):
    print(message, guessed)

def calculate_score(guesses, word):
    points = len(set(word))
    return guesses * points

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''

    guesses = 6
    warnings = 3
    letter_list = []
    # available = get_available_letters(letter_list)
    available = string.ascii_lowercase
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long")
    print("---------")
    while guesses > 0:
        print(f"You have {guesses} guesses left.")
        print(f"Available letters: {available}")
        print("---------")
        guess = str.lower(input('Please guess a letter:'))
        if not str.isalpha(guess):
            warnings -= 1
            print_output(f"Oops! That is not a valid letter. You have {warnings} left:", get_guessed_word(secret_word, letter_list))
            if warnings == 0:
                guesses -= 1
                warnings = 3
                continue
        else:
            letter_list.append(guess)
            if in_secret_word(secret_word, guess):
                print_output("Good guess:", get_guessed_word(secret_word, letter_list))
                if is_word_guessed(secret_word, letter_list):
                    break
            else:
                guesses -= 1
                print_output("Oops! That letter is not in my word:", get_guessed_word(secret_word, letter_list))
                if guesses == 0:
                    break

        available = get_available_letters(letter_list)

    print("---------")

    if is_word_guessed(secret_word, letter_list):
        print("Congratulations, you won!")
        print("Your total score for this game is: ", calculate_score(guesses, secret_word))
    else:
        print(f"Sorry, you ran out of guesses. The word was {secret_word}")

# print(is_word_guessed("monkey", ['m', 'o', 'n', 'k', 'e', 'y']))
# print(get_guessed_word("monkey", ['m', 'n', 'k', 'y']))
# print(get_available_letters(['m', 'n', 'k', 'y']))

hangman("monkey")

# secret_word = choose_word(wordlist)
# hangman(secret_word)
