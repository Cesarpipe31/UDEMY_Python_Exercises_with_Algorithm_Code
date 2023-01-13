"""
Write A Python Program To Get 5 Number From User In Array And Sum All Number And Display
"""

amountArray = int(input("Enter amount array: "))

arraySum = []

for i in range(amountArray):
    arraySum.append(int(input("Enter your number " + str(i+1) + " : ")))

print("Array is: ", arraySum)

sum = 0
for i in arraySum:
        sum += i

print("Array sum is: " + str(sum))

"""
Write a Python Program to get 5 number from user in array, AND find maximum number.
"""

maxNumber = max(arraySum)


print("Maximum number is: " + str(maxNumber))

