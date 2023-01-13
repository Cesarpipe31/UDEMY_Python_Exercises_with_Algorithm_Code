"""
Write a Python Program to get 5 number from user in array, find the maximum number
"""

amountNumber = int(input("Enter amount number: "))

arrayNumber = []

for i  in range(amountNumber):
    arrayNumber.append(int(input("Enter number " + str(i+1) + " :")))

print (arrayNumber)

maximumNumber = max(arrayNumber)

print("Maximum number of array is: " + str(maximumNumber))


"""
Write a Python Program to get 5 number from user in array, find the Minimum number
"""
minimumNumber = min(arrayNumber)

print("Minimum number of array is: " + str(minimumNumber))
