# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "F:\SkyDrive\Studying\MIT_COURSES\IntroToComputerScience_6.001\problemSets\PS03\hangman\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed) :
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for letter in secretWord :
        if letter not in lettersGuessed :
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    resultWord = '' 

    correctLetterList = []
    for letter in lettersGuessed :
        if letter in secretWord :
            if letter not in correctLetterList :
                correctLetterList += letter
                
    i = 0
    for letter in secretWord :
        if letter in correctLetterList :
            resultWord = resultWord + letter
        else :
            resultWord += '_  '
        i += 1
    return resultWord
        



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    availableLetters = ''

    for letter in string.ascii_lowercase :
        if letter not in lettersGuessed :
            availableLetters += letter
    
    return availableLetters

def getAvailableLettersIncludeWrongLetter(lettersGuessed,letter):
    '''
    lettersGuessed: list, what letters have been guessed so far
    letters: string, what letter has been guessed this time
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    lettersGuessed += letter
    getAvailableLetters(lettersGuessed)
    
    return getAvailableLetters(lettersGuessed)

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    secretWordLen = len(secretWord)
    GuessedLetterList = []
    underscores = '_ '
    remainingGuess = 8
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(secretWordLen) \
    + ' letters long.')

    while remainingGuess > 0 :
        print underscores*secretWordLen
        print('You have ' + str(remainingGuess) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(GuessedLetterList))
        guessedLetter = raw_input('Please guess a letter: ')
        guessedLetter = guessedLetter.lower()
        if guessedLetter not in GuessedLetterList :
            GuessedLetterList += guessedLetter
            if guessedLetter in secretWord :
                GuessedWord = getGuessedWord(secretWord, GuessedLetterList)
                print('Good guess: ' + GuessedWord) 
    
                if isWordGuessed(secretWord, GuessedLetterList) :
                    print underscores*secretWordLen
                    print('Congratulations, you won!')
                    return True
            else :

                GuessedWord = getGuessedWord(secretWord, GuessedLetterList)
                print('Oops! That letter is not in my word: ' + GuessedWord)
                remainingGuess -= 1
        else :
            GuessedWord = getGuessedWord(secretWord, GuessedLetterList)
            print("Oops! You've already guessed that letter: " + GuessedWord)    

            
           
       
    
    print underscores*secretWordLen
    print('Sorry, you ran out of guesses. The word was else.')
    return True



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)


def test() :
    
 #   wordlist = loadWords()
  #  secretWord = chooseWord(wordlist)
   # hangman(secretWord)
    secretWord = 'a' 
    lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    print(isWordGuessed(secretWord, lettersGuessed))
    

    print(getGuessedWord(secretWord, lettersGuessed))
    print getAvailableLetters(lettersGuessed)
    hangman(secretWord)

    
test()