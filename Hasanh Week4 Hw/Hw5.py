""""
Date : 22.02.2022
Prepared by the Program : Hasan
Name Of The Program : Random Student
###################################################
///Random Student (Problem Solving Example) General Information: 
I want to choose a random student in Pyton Class-2 Coursiers 
Acceptance Criteria:
Make changes to the random student codes that has been shared with you.
In current state, the program chooses a random one from the list when the button is pressed.
What is expected of you is to ensure that the selected person is not selected during 3 hands. 
(As we talk about in the lesson)
"""
#####################################################################
import random,string
import tkinter as tk

zz_waiting_student=[]
zz_std_list=["Emrullah Bey", "Ertan Bey", "Fethullah Bey", "Furkan Bey", 
    "Hasan Bey", "Mehmet Bey", "Ömer Bey", "Tayyip Bey", 
    "Yunus Emre Bey", "Merve Hanım", "Mustafa Bey", "Murat Bey"]
#####################################################################
def random_student():      
    student = random.sample(zz_std_list, 1)
    print(student)
    zz_waiting_student.append(*student)
    
    str = ''
    for i in student:        
        str += i
    
        indes=(zz_std_list.index(i))
        zz_std_list.pop(indes)
        
    if len(zz_waiting_student)==4:
        zz_std_list.append(zz_waiting_student[0])
        del zz_waiting_student[0]
               
    #print("\nBekleyenler : ",waiting_student)
    #print("\nYeni Liste : ",std_list)
    print(str) 
    label.config(text=str)
    #return str
#####################################################################
window = tk.Tk()

window.title("Random Student")
window.geometry("600x300")


key_application = tk.Frame(window)
key_application.grid()


# label
label_txt = tk.Label(key_application, text="Student name:", font="arial 15 bold")
label_txt.grid(padx=110, pady=10)


# label
label = tk.Label(key_application, text="Please push the botton to choose a next student ", font="arial 12")
label.grid(padx=110, pady=20)


# button
button1 = tk.Button(key_application, text=" CHOOSE ", width=50, height=5, command=random_student)
button1.grid(padx=110, pady=40)

window.mainloop()

#####################################################################