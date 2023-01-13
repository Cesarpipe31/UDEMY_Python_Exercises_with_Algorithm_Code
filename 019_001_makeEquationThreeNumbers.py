"""
Write A Python Program To Get 3 Number From User And Put In The Following Equation:
        a+b+ca/b(2a + 3b)
"""

numberA = int(input("Enter number integer A : "))
numberB = int(input("Enter number integer B : "))
numberC = int(input("Enter number integer C : "))


result = (numberA + numberB + numberC) * (numberA/numberB) * (2*numberA + 3*numberB)

print("\nResult is: ",result)

"""
Write A Python Program To Get 4 Number From User And Put In The Following Equation:
d+a+2ab/d(4c+10)
"""

numberD = int(input("\nEnter number integer D : "))

result1 =  numberD+numberA+((2*numberA*numberB)/(numberD*(4*numberC+10)))

print("\nResult1 is: ",result)
