""""
Date : 22.02.2022
Prepared by the Program : Hasan
Name Of The Program : Calculator
###################################################
///Calculator: General Information: 
I want to use a program which can calculate basic mathematical operations.
Acceptance Criteria:
The calculator must support the Addition, Subtraction, Multiplication
and Division operations.
All operations must be in a different module as method.
Operations must define with two float numbers as parametres.
Use math.ceil() for all results.
Create a menu to choose an operation.
User can choose invalid options, so you must handle all possible error.
(Use try except :))
Inform user what type of error occured (TypError, ValueError etc.)
This process must continue until user want to quit from calculator.
///
"""
#####################################################################

from time import sleep, time
import operations,math,sys



while True:    #The purpose of the TRUE loop here is to run the program until the user wants to exit.

    print("\n************CALCULATOR************")
    
    try :       #All situations that may occur by the user are written in the TRY block.
    
        n=str(input("""\nEnter the number you want to operations : 
                    1.ADDITION
                    2.SUBTRACTION
                    3.MULTIPLICATION
                    4.DIVISION
                    5.EXIT
                    \n """))
        if n=='5':                              
            print("Calculator Shuts Down...")
            sleep(2)                # Added 2 second wait while closing the program.
            print("Have a nice day!")
            break
            
        
        elif n=='1':
            x=float(input("Enter the first number : "))
            y=float(input("Enter the second number : "))
            z=operations.Addition(x,y) # The Addition Function of the OPERATIONS module has been called.
            w=math.ceil(z)   #The result is rounded up to one larger number with the math.ceil() function.
            print(x,"+",y,"=",w)
        
        elif n=='2':
            x=float(input("Enter the first number : "))
            y=float(input("Enter the second number : "))
            z=operations.Subtraction(x,y) # The Subtraction Function of the OPERATIONS module has been called.
            w=math.ceil(z)   #The result is rounded up to one larger number with the math.ceil() function.
            print(x,"-",y,"=",w)
        
        elif n=='3':
            x=float(input("Enter the first number : "))
            y=float(input("Enter the second number : "))
            z=operations.Multiplication(x,y) # The Multiplication Function of the OPERATIONS module has been called.
            w=math.ceil(z)  #The result is rounded up to one larger number with the math.ceil() function.
            print(x,"*",y,"=",w)
        
        elif n=='4':
            x=float(input("Enter the first number : "))
            y=float(input("Enter the second number : "))
            z=operations.Division(x,y)  # The Division Function of the OPERATIONS module has been called.
            w=math.ceil(z)  #The result is rounded up to one larger number with the math.ceil() function.
            print(x,"/",y,"=",w)
        
        else : 
            print("You have entered incorrectly. Try again. ")
            continue
        
#####################################################################    
    except:    #This part will work when there is a problem inside the TRY block.
        print("\nYou have entered incorrectly. Try again.")
        #print(sys.exc_info()[0])
        
        text1=str(sys.exc_info()[0])

        print("Your error :******",text1.split("'")[1],"******\n")
        
#####################################################################
        
    
        
    
    


