"""
Write A Program To Get 6 Number In The List And Display All Number And Then Clear List And Then Display
"""

amountNumbers = int(input("Enter amount numbers: "))

listNumbers = []

for i in range(amountNumbers):
    listNumbers.append(int(input("Enter your number " + str(i+1) + " : ")))

print("\nThis is the list: ", listNumbers)

listNumbers.clear()
print ("\n Now, we have removed the list item")
print("\nThis is new list whith removed items : ", listNumbers)
