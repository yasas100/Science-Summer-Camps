import random
randomNumber=random.randint(1,10)
usrGuess= int(input("Guess a number between 1 and 10 \n"))
if(usrGuess==randomNumber):
    print("Congratulations your guess was correct!")
else:
    print("Incorrect Guess, the number was "+ str(randomNumber) + " ,please play again")
                