""""
Date : 22.02.2022
Prepared by the Program : Hasan
Name Of The Program : Requests
###################################################
///Requests General Information: 
I want to choose random information with the requests module. Acceptance Criteria:
Get the name, surname, city and country information of a random person by using the requests module. 
(Example=> name:Amber, surname: Murray, city: Salisbury, country: United Kingdom)
Make lowercase and adjacent by removing the spaces. (Example=> ambermurraysalisburyunitedkingdom)
Then randomly shuffle the location of all the characters. 
(Example=> mberarrumasyarubsiluniydetmdoingk)
Apply this process for 100 different people and write in a list.
Find that has the most characters and print it.
"""
#####################################################################
from black import mask_cell
import requests,random,time,datetime


maxim=0
now=datetime.datetime.now()
for i in range(5):  

    r = requests.get("https://randomuser.me/api/")
    name= r.json()["results"][0]["name"]["first"]
    surname=r.json()["results"][0]["name"]["last"]
    city=r.json()["results"][0]["location"]["city"]
    country=r.json()["results"][0]["location"]["country"]

    all=name+surname+city+country
    all1="".join(all.split()).lower()
    my_list=list(all1)
    random.shuffle(my_list)

    my_str=""
    for j in my_list:
        my_str+=j

    print(my_str)
    print("len= ",len(my_str))
    
    if len(my_str)>maxim:
        maxim=len(my_str)        
        max_my=my_str
#####################################################################
know=datetime.datetime.now()
know_time=know-now
  
print("\n\nMaximum info = ", max_my)        
print("\nLength of Maximum ",maxim,"\n")  
print("competed ",know_time.seconds,"seconds.")
#####################################################################




