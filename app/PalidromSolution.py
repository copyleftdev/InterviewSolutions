#!/usr/bin/env python
#author: Don Johnson
#email: <dj@codetestcode.io>

import string

def detectPalidromWordSimple(word):
     myWord = word.lower()
     revWord = list(reversed(myWord))
     if list(myWord) == list(revWord):
         return True
     else:
         return False

def detectPalidromSentence(sentence):
    sentenceToLower = sentence.lower()
    sentence = ''.join(sentenceToLower.split())
    revSentence = list(reversed(sentenceToLower))

    if list(sentenceToLower) == list(revSentence):
        return True
    else:
        return False

def detectPalidromWordWithPunctuations(word):
    excludedChars ='''! ( ) - [ ] { } ; : ' " \ , < > . / ? @ # $ % ^ & * _ ~'''
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





PalidromWordList = ["bob","BoB","wow","BOB","WOW", "WoW","test"]

PalidromSentenceList = ["Sore was I ere I saw Eros","Noel sees Leon",
                        "test a non palidrom"
                       ]
PalidromPunctuationList = ["!test","t.est.","wow","wow!.","w.!:o.W;"]




# for eachWord in PalidromWordList:
#     print(detectPalidromWordSimple(eachWord))
#
# for eachSentence in PalidromSentenceList:
#     print(detectPalidromSentence(eachSentence))

# for eachWord in PalidromPunctuationList:
#     print(detectPalidromSentence(eachWord))
for eachWord in PalidromPunctuationList:
    print(detectPalidromWordWithPunctuations(eachWord))
