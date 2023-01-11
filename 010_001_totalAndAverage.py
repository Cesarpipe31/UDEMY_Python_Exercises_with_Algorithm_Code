"""
Write A Python Program to get 6 subject marks from the user and calculate total and average of that marks. 
And display to user.
"""
subject1 = float (input("Enter subject mark 1: "))
subject2 = float (input("Enter subject mark 2: "))
subject3 = float (input("Enter subject mark 3: "))
subject4 = float (input("Enter subject mark 4: "))
subject5 = float (input("Enter subject mark 5: "))
subject6 = float (input("Enter subject mark 6: "))

total = subject1 + subject2 + subject3 + subject4 + subject5 + subject6
average = total / 6

print ("Total is " + str(total) + " and your average is " + str(average))
    


"""
Write A Python Program to get 6 subject marks from the user and calculate total, average and percentage of that marks.
And display to user.
"""

print("\n")

percentageSubject1 = subject1 / total
print("Percentage subject1 is "  + str(percentageSubject1))

percentageSubject2 = subject2 / total
print("Percentage subject2 is " + str(percentageSubject2))

percentageSubject3 = subject3 / total
print("Percentage subject3 is " + str(percentageSubject3))

percentageSubject4 = subject4 / total
print("Percentage subject4 is " + str(percentageSubject4))

percentageSubject5 = subject5 / total
print("Percentage subject5 is " + str(percentageSubject5))

percentageSubject6 = subject6 / total
print("Percentage subject6 is " + str(percentageSubject6))

