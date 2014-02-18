# hangman.py

import random

HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''

  +---+
  |   |
 [O   |
 /|\  |
 / \  |
      |
=========''', '''

  +---+
  |   |
 [O]  |
 /|\  |
 / \  |
      |
=========''']

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar coyote'
      +  'crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion'
      +  'lizard llama mole monkey moose mouse mule newt otter owl panda parrot '
      +  'pigeon python rabbit ram rat raven rhino salmon seal shark sheep '
      +  'skunk sloth snake spider stork swan tiger toad trout turkey turtle '
      +  'weasel whale wolf wombat zebra red orange yellow green blue indigo '
      +  'violet white black brown square triangle rectangle circle ellipse '
      +  'rhombus trapazoid chevron pentagon hexagon septagon octogon apple '
      +  'orange lemon lime pear watermelon grape grapefruit cherry banana '
      +  'cantalope mango strawberry tomato').split()

def getRandomWord (wordList):
    """
    Returns a random string from the passed list of strings.
    """
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard (HANGMANPICS, missedLetters, correctLetters, secretWord):
    """
    Prints the game board to the console.
    """
    # Print the current hangman pic.
    print(HANGMANPICS[len(missedLetters)])
    print()
    
    # Print the current missed letters.
    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    # replace blanks with correctly guessed letters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    
    # show the secret word with spaces in between each letter
    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess (alreadyGuessed):
    """
    Returns the letter the player entered. This function makes sure the player
    entered a single letter, and not something else.
    """
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER! (e.g. a, b, c... etc.)')
        else:
            return guess

def playAgain ():
    """
    Returns TRUE if the player wants to play again,
    otherwise it returns FALSE.
    """
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

# Main game loop
while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    # Let the player type in a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nYou were hanged!\nAfter '
                  + str(len(missedLetters)) + ' missed guesses and '
                  + str(len(correctLetters)) + ' correct guesses, the word '
                  + 'was "' + secretWord + '".')
            gameIsDone = True

    # Ask the player if they want to play again if the game is done.
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
