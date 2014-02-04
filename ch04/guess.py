# This is a guess the number game
import random
import math

guessesTaken = 0
rangeHighValue = 100
rangeLowValue = 1
numGuesses = math.ceil(math.log((rangeHighValue + 1), 2))

print("Hello! What is you name?")
userName = input()

number = random.randint(rangeLowValue, rangeHighValue)
print("Well, " + userName + ", I am thinking of a number between "
      + str(rangeLowValue) + " and " + str(rangeHighValue) + ".")
print("You have " + str(numGuesses) + " guesses.")

while guessesTaken < numGuesses:
    print("Take a guess.")
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print("Your guess is too low.")

    if guess > number:
        print("Your guess is too high.")

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print("Good job, " + userName + "! You guessed my number in "
          + guessesTaken + " guesses!!!");

if guess != number:
    number = str(number)
    print("Nope! The number I was thinking of was " + number + ".")

