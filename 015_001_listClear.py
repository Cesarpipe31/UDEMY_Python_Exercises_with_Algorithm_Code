"""
Write A Program To Get 6 Number In The List And Display All Number And Then Clear List And Then Display
"""

amountNumbers = int(input("Enter amount numbers: "))

listNumbers = []

for i in range(amountNumbers):
    listNumbers.append(int(input("Enter your number " + str(i+1) + " : ")))

print("\nThis is the list: ", listNumbers)

tupleNumber = tuple((listNumbers)) #se registra la instrucción antes de borrar la lista



listNumbers.clear()
print ("\n Now, we have removed the list item")
print("\nThis is new list whith removed items : ", listNumbers)



"""
Write A Program To Get 6 Number In The TUPLE And Display All Number And Then Clear TUPLE And Then Display
"""

#tupleNumber = tuple((listNumbers)) #se registra la instrucción antes de borrar la lista

print("\nThis is a tuple : ", tupleNumber)

listNumber1 = list(tupleNumber)
listNumber1.remove()

tupleNumber = tuple(listNumber1)

print("\nThis is a tuple clear : ", tupleNumber)






