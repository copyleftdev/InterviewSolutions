#!/usr/bin/env python
#author: Don Johnson
#email: <dj@codetestcode.io>
# -*- coding: utf-8 -*-


 #Step 1.
 #Find the total length of the given string " We love working for Guidance Software, Inc" 
 
 #Step 2.
 #With the provided values (21,31,18,24,3,9,5,11,12) create a new string with an expected 
 #result of "Good Work"


GivenString = "We love working for Guidance Software, Inc"
exspectedString = "Good Work"
G = GivenString[31-11]
o = GivenString[9]
d = GivenString[11+12]
W = GivenString[21-21]
r = GivenString[5+5]
k = GivenString[11]


result = "{}{}{}{} {}{}{}{}".format(G,o,o,d,W,o,r,k)

print(result)


