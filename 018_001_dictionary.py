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

