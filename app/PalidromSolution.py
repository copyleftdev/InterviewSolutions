#!/usr/bin/env python
#author: Don Johnson
#email: <dj@codetestcode.io>
 
# Step 1:
# Write a function, that given a string will determine if the string is a
# palindrome and return true if it is, and false if not.
 
# A Palindrome is a word, phrase, number or other sequence of characters which reads
# the same backwards as forward.  Allowances may be made for adjustments to capital 
# letters, punctuation, and word dividers.
 
# example of a Palindrome: "wow"
 
# Step 2:
# Write a function to test your program, providing adequate variations of input to 
# properly test the algorithm.

import string

def isPalindrom(inputString):
    convertToLowerCase = inputString.lower()
    stripedSpaces = ''.join(convertToLowerCase.split())
    charExcludeList = []

    excludedChars ='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    for eachChar in excludedChars:
        charExcludeList.append(eachChar)

    

    for punct in string.punctuation:
        if punct in charExcludeList:
            stripedSpaces = stripedSpaces.replace(punct,"")

    MyString = stripedSpaces
    RevString = list(reversed(stripedSpaces))

    if list(MyString) == list(RevString):
        return True
    else:
        return False

#Test Datasets
PalidromVariantsListTrue = [ "wow", ":Wo.W!", "WOW", "111","Sore was I ere I saw Eros",
                              "Sore [ ] { } ; : ' was I ere I sa@ # $ % ^w Eros"]

PalidromVariantsListFalse = ["This text is not a palindrome.",'Don','123456','Guidance Sofrware',
                              "Sore [ ] { } ; : ' was I ere I sa@ # $ % ^w Eross"]

# Testing Logic 
print("#Testing Truth Dataset")
for eachValue in PalidromVariantsListTrue:
    print("{}:{}".format(eachValue,isPalindrom(eachValue)))
print("\n")

print("#Testing False Dataset")
for eachValue in PalidromVariantsListFalse:
    print("{}:{}".format(eachValue, isPalindrom(eachValue)))
print("\n")