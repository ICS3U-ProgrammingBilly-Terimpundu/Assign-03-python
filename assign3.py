#!/usr/bin/env python3

# Created by Billy Terimpundu
# Created on December 2021
# This program checks whether an entered character
# is lowercase or uppercase by using ASCII.

# Take the Input From the User
ch = input("Enter Any Character: ")

if(ord(ch) >= 97 and ord(ch) <= 122):
    print("The Given Character", ch, "is a Lowercase Alphabet")
    
elif(ord(ch) >= 65 and ord(ch) <= 90):
    print("The Given Character", ch, "is a Uppercase Alphabet")
    
else:
    print("The Given Character", ch, "is Not an Alphabet")