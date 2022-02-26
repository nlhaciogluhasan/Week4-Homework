""""
Date : 22.02.2022
Prepared by the Program : Hasan
Name Of The Program : Number Guessing Game
###################################################
///Number Guessing Game General Information: 
I want to play a game which I can guess a number. The computer chooses a number in the range I chose. 
So that I can try to find the correct number which was selected by computer. 
Acceptance Criteria:
Computer must randomly pick an integer from user selected a range, i.e., from A to B, 
where A and B belong to Integer. Your program should prompt the user for guesses 
if the user guesses incorrectly, it should print whether the guess is too high or too low.
If the user guesses correctly, the program should print total time and total number of guesses.
You must import some required modules or packages You can assume that the user will enter valid input.
"""
#####################################################################

import random,time,datetime

A=int(input("What number should be the starting point of the number you want to guess? : "))
B=int(input("What number should be the finishing point of the number you want to guess? : "))
number=random.randint(A,B)
#print(number)

guess_count=0

print("The time has now begun : ")
now=datetime.datetime.now()

#####################################################################
while True:
    your_guess=int(input("What is your guess :"))
    if your_guess>number:
        print("Your guess is too high. ")
        guess_count+=1

    elif your_guess<number:
        print("Your guess is too low. ")
        guess_count+=1
        
    else :
        know=datetime.datetime.now()
        know_time=know-now
        print("Congratulations. You guessed the number correctly.")
        guess_count+=1
        print("You know in the",guess_count,".guess.")
        print("You knew it in ",know_time.seconds,"seconds.")
        break
#####################################################################    


