"""
Write A Python Program To Get Number From The User, And Display Table For That Number.
"""

number = int(input("Enter your number: "))
print("Your number is " + str(number))

for i in range(1,11):
    print(str(i) + " X " + str(number) + " is: " + str(i*number))
    


"""
Write A Python Program To Get 2 Number From The User, And Display 2 Table For That Number.
"""

number1 = int(input("Enter your number one: "))
number2 = int(input("Enter your number two: "))

for i in range(1,11):
    print(str(i) + " X " + str(number1) + " is: " + str(i*number1))

for j in range(1,11):
    print(str(j) + " X " + str(number2) + " is: " + str(j*number2))
