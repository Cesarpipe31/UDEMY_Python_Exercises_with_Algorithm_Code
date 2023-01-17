"""
    Write A Python Program To Get Two Number And Operator From The User To Perform Arithmetic Operation
"""

numberFirst = int(input("Enter number first: "))
numberSecond = int(input("Enter number second: "))
mathematicOperator = input("Enter your operator ( +  ó  -  ó  *  ó  /  ó  %  )  :  ")
result = 0

if (mathematicOperator == "+"):
    result = numberFirst + numberSecond
    print ("Result addition numberFirs + numberSecond is: " + str(result))

if (mathematicOperator == "-"):
    result = numberFirst -+ numberSecond
    print ("Result subtraction numberFirs - numberSecond is: " + str(result))

if (mathematicOperator == "*"):
    result = numberFirst * numberSecond
    print ("Result multiplication numberFirs * numberSecond is: " + str(result))

if (mathematicOperator == "/"):
    result = numberFirst / numberSecond
    print ("Result division numberFirs / numberSecond is: " + str(result))

if (mathematicOperator == "%"):
    result = numberFirst % numberSecond
    print ("Result module numberFirs % numberSecond is: " + str(result))






