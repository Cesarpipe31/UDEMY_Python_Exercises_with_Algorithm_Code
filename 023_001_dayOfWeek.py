"""
Write a Python program get name of week and show “Holiday” if user input Sunday
"""
    
dayWeek = input("Enter day of week: ")

if (dayWeek == "Sunday"):
    print(str(dayWeek) + " is " + str("Holidady"))


    """
Write a Python program get name of week and show “Holiday” if user input Sunday or Friday
    """

if (dayWeek == "Sunday" or dayWeek == "Friday"):
    print(str(dayWeek) + " is " + str("Holiday"))
