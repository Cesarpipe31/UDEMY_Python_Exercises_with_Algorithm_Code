"""Write a Python program to display following output using for loop 
*
* * 
* * *
* * * * 
* * * * *
"""

for i in range(6):
    for j in range (i):
        print("*", end=" ")
    print("")


"""
Write a Python program to display following output using for loop 
                                                    *
                                                 *  * 
                                                * * *
                                              * * * * 
                                            * * * * *
"""


for i in range(6):
    for j in range (i):
        print("\t\t\t\t\t\t\t","*", end=" ")
    print("")

