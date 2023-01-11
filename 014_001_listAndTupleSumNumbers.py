"""
Write A Program To Get 6 Number In The List And Sum That Number 
"""
amountNumbers = int(input("Enter amount numbers: "))

listNumber = []

for i in range(amountNumbers):
    listNumber.append(int(input("Enter integer number " + str(i+1) + ": ")))

print(listNumber)

sumNumbers = 0

for i in listNumber:
    sumNumbers += i

print("\nSum integers numbers is: " + str(sumNumbers))


"""
Write a program to get 6 number in the TUPLE and sum that number 
"""

tupleNumber = tuple(listNumber)

print("\n This is a tuple: ", tupleNumber)
print(type(tupleNumber))

sumTupleNumbers = 0

for i in tupleNumber:
    sumTupleNumbers += i


print("\n\nSum integers numbers in tuple is: " + str(sumTupleNumbers))

