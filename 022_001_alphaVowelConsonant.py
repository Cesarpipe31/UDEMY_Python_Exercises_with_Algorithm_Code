"""
Write A Python Program To Check Alpha Character, Whether Vowel Or Consonant
"""

"""
char = (input("Enter your character: "))


if (char == "a" or char == "e" or char == "i" or char == "o" or char == "u"):
    print("Character is vowel: " +char)
else:
    print("Character is consonant: " +char)
"""

"""
Write a Python program to check alpha character, whether vowel or consonant. 
And also display “it is number”, if user give any number.
"""


char = (input("Enter your character, aphabetic o number: "))


if (char == "a" or char == "e" or char == "i" or char == "o" or char == "u"):
    print("Character is vowel: " +char)
elif (char =="9" or char == "8" or char == "7" or char == "6" or char == "5" or char == "4" or char == "3" or char == "2" or char == "1" or char == "0"):
    print("Character is number: " +char)
else:
    print("Character is consonant: " +char)
