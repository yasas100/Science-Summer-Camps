import time
import random
def main():
    plays=["Rock","Paper","Scissors"]
    print("Welcome to the rock paper scissors game")
    time.sleep(1.5)
    usrPick= input("Please choose rock paper or scissors.(r/p/s) ").lower()
    if(usrPick=='r'):
        usrPick=int(1)
    elif(usrPick=='p'):
        usrPick=int(2)
    elif(usrPick=='s'):
        usrPick=int(3)
    else:
        print("Invalid input")
        return()
    computerPick=random.randint(1,3)
    if(computerPick==1):
        if(usrPick==1):
            print("Its a tie. Computer chose Rock")
        elif(usrPick==2):
            print("You Win! Computer chose Rock")
        elif(usrPick==3):
            print("You loose! Computer chose Rock")
    if(computerPick==2):
        if(usrPick==1):
            print("You loose! Computer chose Paper")
        elif(usrPick==2):
            print("Its a tie. Computer chose Paper")
        elif(usrPick==3):
            print("You Win! Computer chose Paper")       
    if(computerPick==3):
        if(usrPick==1):
            print("You Win! Computer chose Scissors")
        elif(usrPick==2):
            print("You loose! Computer chose Scissors")
        elif(usrPick==3):
            print("Its a tie.Computer chose Scissors")       
    
main()

