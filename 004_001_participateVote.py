"""
Write A Python Program To Take Age From The User To Check Whether User Able To Participate In Voting Or Not. 
If Age Is Less Than 18 Then It Don’t Allow To Participation. And Show, After How Much Year A Person Will Be 
Able To Participate:

Expected Result if user input 10 year then:
Sorry! You cannot participate in voting, you will be able to participate after 8 year


Write A Python Program To Take Marks From The User To Check Whether User Able To Admission In College Or Not. 
If Marks Is Less Than 60 Then It Don’t Allow To Take Admission. 

Expected Result if user input 50 year then:
Sorry! You cannot take admission, you need 10 numbers more to take admission
"""

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if (age >= 18):
    print ("Hi " + name + "!. You Able To Participate In Voting")
elif (age == 10):
    print ("Hi " + name + ". Sorry! You cannot participate in voting, you will be able to participate after 8 year")
else: 
    print ("Hi " + name + "!. It Don’t Allow To Participation")
    
    


