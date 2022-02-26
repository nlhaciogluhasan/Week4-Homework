""""
Date : 22.02.2022
Prepared by the Program : Hasan
Name Of The Program : Random Password
###################################################
///Random Password General Information: 
I want to use a program which can generate random password and 
display the result on user interface. 
Acceptance Criteria:
Use tkinter package to solve the problem. 
(You can use the random student codes as template)
Password length must be 10 characters long.
It must contain at least 2 upper case letter, 2 digits and 
2 special symbols.
You must import some required modules or packages.
The GUI of program must contain at least a button and a label 
(customize the screen according to yourself)
The result should be display on the password label when the user 
click the generate button.
"""
#####################################################################

import random,string
import tkinter as tk
from ntpath import join
from string import ascii_letters, ascii_lowercase, ascii_uppercase
#####################################################################

def random_password():
    my_password=[]
    for i in range (2):
        my_password.append(list(ascii_uppercase)[random.randint(0,(len(list(ascii_uppercase))-1))])
        my_password.append(list(string.digits)[random.randint(0,(len(list(string.digits))-1))])
        my_password.append(list(string.punctuation)[random.randint(0,(len(list(string.punctuation))-1))])

    for i in range(4):
        my_password.append((list(string.printable))[:-11][random.randint(0,(len((list(string.printable))[:-11])-1))])

    random.shuffle(my_password)
    print(''.join(my_password))
        
    label.config(text=my_password)
    my_password=[]
    #return str

#####################################################################
window = tk.Tk()

window.title("Random Password")
window.geometry("600x300")


key_application = tk.Frame(window)
key_application.grid()


# label
label_txt = tk.Label(key_application, text="Password:", font="arial 15 bold")
label_txt.grid(padx=110, pady=10)


# label
label = tk.Label(key_application, text="Please push the botton to choose a next password ", font="arial 12")
label.grid(padx=110, pady=20)

# button
button1 = tk.Button(key_application, text=" CHOOSE ", width=50, height=5, command=random_password)
button1.grid(padx=110, pady=40)

window.mainloop()
#####################################################################