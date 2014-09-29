import random

def getSecretNum(numDigits):
    """
    Returns a string that is numDigits long, made up of unique random digits.
    """
    numbers = list(range(10))
    random.shuffle(numbers)
    
    secretNum = ''
    for i in range(numDigits):
        secretNum += str(numbers[i])

    return secretNum

def getClues(guess, secretNum):
    """
    Returns a string with the pico, fermi, bagels clues to the user.
    """
    if guess == secretNum:
        return 'You got it!'

    clue = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clue.append('Fermi')
        elif guess[i] in secretNum:
            clue.append('Pico')

    if len(clue) == 0:
        return 'Bagels'

    clue.sort()

    return ' '.join(clue)

def isOnlyDigits(num):
    """
    Returns True if num is a string made up of only digits.
    Otherwise returns False.
    """
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True
