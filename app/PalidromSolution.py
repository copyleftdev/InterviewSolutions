# !/usr/bin/env python
# author: Don Johnson
# email: <dj@codetestcode.io>
 
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

def detectPalindromWordSimple(word):
     myWord = word.lower()
     revWord = list(reversed(myWord))
     if list(myWord) == list(revWord):
         return True
     else:
         return False

def detectPalindromSentence(sentence):
    sentenceToLower = sentence.lower()
    sentence = ''.join(sentenceToLower.split())
    revSentence = list(reversed(sentenceToLower))

    if list(sentenceToLower) == list(revSentence):
        return True
    else:
        return False

def detectPalindromWordWithPunctuations(word):
    excludedChars ='''! ( ) - [ ] { } ; : ' " \ , < > . / ? @ # $ % ^ & * _ ~ + = | ~'''
    CharExcludeList = excludedChars.split()
    for punct in string.punctuation:
        if punct in CharExcludeList:
            word = word.replace(punct,"")
    myWord = word.lower()
    RevWord = list(reversed(myWord))

    if list(myWord) == list(RevWord):
        return True
    else:
        return False




#Test Data
PalindromWordList = ["bob","BoB","wow","BOB","WOW", "WoW","test"]

PalindromSentenceList = ["Sore was I ere I saw Eros","Noel sees Leon",
                        "test a non Palindrom"
                       ]
PalindromPunctuationList = ["!test","t.est.","wow","wow!.","w.!:o.W;",
                        "!@#w$%^o~w&*()_+-"
                          ]


#Function tests
print("Testing detectPalindromWordSimple")
for eachWord in PalindromWordList:
    print("{}:{}".format(eachWord,detectPalindromWordSimple(eachWord)))
print("\n"*2)

print("Testing detectPalindromSentence")
for eachSentence in PalindromSentenceList:
    print("{}:{}".format(eachSentence,detectPalindromSentence(eachSentence)))
print("\n"*2)

print("Testing detectPalindromWordWithPunctuations")
for eachWord in PalindromPunctuationList:
    print("{}:{}".format(eachWord,detectPalindromWordWithPunctuations(eachWord)))
print("\n"*2)
