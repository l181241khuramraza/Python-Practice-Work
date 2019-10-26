###### Game: 'Guess a Number' without using Function #######
import random
secretNumber = random.randint(1,100)
print("You are to choose a number between 1 and 100 including 1&100 to play")
for numberOfGuesses in range(1,7):
    guessedNumber=input()
    guessedNumber=int(guessedNumber)
    if(guessedNumber > secretNumber):
        print("Your number is greater than the number to be guessed")
    elif (guessedNumber < secretNumber):
        print("your number is lower than the number to be guessed")
    else:
        break;

if(guessedNumber == secretNumber):
    print("you won the game in"+ str(numberOfGuesses) +" effort.")
else:
    print("You lost the game")
