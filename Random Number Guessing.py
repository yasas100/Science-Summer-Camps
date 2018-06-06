import random
playagain=True
while (playagain):
    randomNumber=random.randint(1,10)
    usrGuess= int(input("Guess a number between 1 and 10 \n"))
    if(usrGuess==randomNumber):
        print("Congratulations your guess was correct!")
    else:
        print("Incorrect Guess, the number was "+ str(randomNumber) )
        #playagain1= input("Would you like to play again (y/n)").lower
    if((input("Would you like to play again (y/n)")).lower()=="y"):
        playagain=True
    else:
        playagain=False
                    