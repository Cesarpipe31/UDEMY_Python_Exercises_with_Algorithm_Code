"""
Write A Python Program to store name, address, contact in dictionary, and then update his/her contact number 
"""

userInfo = {
    "name": "Cesar",
    "address": "Cra 6b",
    "contact": "317317317"
    }

print("Print my first record: " , userInfo)

userInfo.update({"contact": "320320320"})

print("Print my update record: " , userInfo)


""""
Write A Python Program to store name, address, contact in dictionary, and then update user contact number,  but user will enter his/her contact number at run time.
"""

numberContact =  input("Enter your number contact: ")

userInfo["contact"] = numberContact

print("New dictionary: ", userInfo)