"""
Write A Python Program To Get 2 Number From The User And Display Maximum Number 
"""

number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

if (number1 > number2):
    print ("Number " + str(number1) + " is more greater that number " + str(number2))
elif (number2 > number1):
    print ("Number " + str(number2) + " is more greater that number " + str(number1))
else:
    print ("Number " + str(number1) + " is equal to number " +str(number2))

maxNumber = max(number1, number2)
print ("Maximun number is : " + str(maxNumber))


""""
Write A Python Program To Get 3 Number From The User And Display Maximum Number 
"""

number3 = int(input("Enter number 3: "))

if(number1 > number2 and number1 > number3 ):
    print(str(number1) + " is maximun")
elif (number2 > number1 and number2 > number3):
    print(str(number2) + " is maximun")
elif (number3 > number1 and number3 > number1):
    print(str(number3) + " is maximun")
else:
    print(str(number1) + " , " + str(number2) + " , " + str(number3) + " are equals")

maxNumber1 = max(number1, number2, number3)
print ("Maximun that three numbers is " + str(maxNumber1))