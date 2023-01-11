"""
Write Python Program To Get Password From User And Make Sure That Password Should Contain Number And Alphabetic 
"""

password = input("Enter your password: ")

print("Option 1: Alphanumeric")
if(password.isalnum()):
    print ("Password is correct, is alphanumeric")
else:
    print ("Please, change your password, only alphanumeric")


"""
Write Python Program To Get Password From User And Make Sure That Password Should Contain Number 
And Alphabetic AND Password Length Should Not Be Greater Than Or Equal To 8 
"""

print("\nOption 2: Alphanumeric and maximun 8 characters")
if(password.isalnum() and len(password) <= 8):
    print ("Password is correct, is alphanumeric and your length is maximun 8")
else:
    print ("Please, change your password, only alphanumeric and must have maximun 8 characters")
