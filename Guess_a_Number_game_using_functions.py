###### Game: 'Guess a Number' using Function #######
import random
secretNumber = random.randint(1,100) ## randit return random number btwn 1 and 100 including them

### function definition

def guessANumberGame():
    global numberOfGuesses ## global variable statement
    for numberOfGuesses in range(1,7):
        guessedNumber=input()
        guessedNumber=int(guessedNumber)
        if(guessedNumber > secretNumber):
            print("Your number is greater than the number to be guessed")
            if(numberOfGuesses+1==7):
                return guessedNumber
        elif (guessedNumber < secretNumber):
            print("your number is lower than the number to be guessed")
            if(numberOfGuesses+1==7):
                return guessedNumber
        else:
            return guessedNumber


numberOfGuesses=1
print("You are to choose a number between 1 and 100 including 1&100 to play")

### function calling

if(guessANumberGame() == secretNumber):
    print("you won the game in "+ str(numberOfGuesses) +" effort.")
else:
    print("You lost the game")
