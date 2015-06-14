#!/usr/bin/env python
#author: Don Johnson
#email: <dj@codetestcode.io>
# -*- coding: utf-8 -*-
 
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
import unittest

def isPalindrome(inputString):
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

#Unit tests for isPalindrome
class TestPalindrome(unittest.TestCase):

    def test_palindrome_lowercase_string_single_word(self):
        self.word = "wow"
        self.assertVector = isPalindrome(self.word);
        self.assertEquals(self.assertVector,True)
    
    def test_palindrome_uppercase_string_single_word(self):
        self.word = "WOW"
        self.assertVector = isPalindrome(self.word);
        self.assertEquals(self.assertVector,True)
    
    def test_palindrome_mixedcase_string_single_word(self):
        self.word = "wOw"
        self.assertVector = isPalindrome(self.word);
        self.assertEquals(self.assertVector,True)

    def test_non_palidrome_lowercase_string_single_word(self):
        self.word = "test"
        self.assertVector = isPalindrome(self.word)
        self.assertEquals(self.assertVector, False)
    
    def test_non_palindrome_lowercase_string_single_word(self):
        self.word = "dfe"
        self.assertVector = isPalindrome(self.word);
        self.assertEquals(self.assertVector,False)
    
    def test_non_palindrome_uppercase_string_single_word(self):
        self.word = "dfe"
        self.assertVector = isPalindrome(self.word);
        self.assertEquals(self.assertVector,False)
    
    def test_non_palindrome_mixedcase_string_single_word(self):
        self.word = "dfe"
        self.assertVector = isPalindrome(self.word);
        self.assertEquals(self.assertVector,False)

    def test_palindrome_sentence(self):
        self.sentence = "Deliver desserts demanded Nemesis emended named stressed reviled."
        self.assertVector = isPalindrome(self.sentence)
        self.assertEquals(self.assertVector, True)
    
    def test_non_palindrome_sentence(self):
        self.sentence = "Deliver desserts demanded Nemesis emended named stressed reviled. false"
        self.assertVector = isPalindrome(self.sentence)
        self.assertEquals(self.assertVector, False)

    def test_palindrome_single_word_with_punctuations(self):
        self.word = '''!"#$%&'(w)*+,-./:;<=>?@[o\]^_`{|w}~'''
        self.assertVector = isPalindrome(self.word)
        self.assertEquals(self.assertVector, True)
    
    def test_palindrome_single_word_with_punctuations(self):
        self.word = '''!"#$%&'(w)*+,-./:;<=>?@[o\]^_`{|w}~'''
        self.assertVector = isPalindrome(self.word)
        self.assertEquals(self.assertVector, True)
    
    def test_non_palidrome_single_word_with_punctuations(self):
        self.word = '''!"#$%&'(d)*+,-./:;<=>?@[o\]^_`{|w}~'''
        self.assertVector = isPalindrome(self.word)
        self.assertEquals(self.assertVector, False)
    
    def test_multi_line_non_palindrome_punctuation(self):
        self.multi_line = """Dennis, Nel~@@@@@@l,11 Edna, Leon, Nedra, Ani~~~~ta, Rolf~~~, Nora,
                             Alice, Carol, Leo, Jane, Reed, Dena, D~~ale, Basil, Rae,
                            Penny, Lana, Dave, De!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~nny, 
                            Lena, Ida, Bernad!!!!!!~~ette, Ben, Ray, 
                            Lila, Nina, Jo, Ira, Mara, Sara, Mar!~~io, Jan, Ina, Lily, Arne,
                            Bette, Dan, Reba, Diane, Lynn, !"#$%&'()*+,-./:;<=>?@[\]^_`{Ed|}~, Eva, Dana, Lynne, Pearl, Isabel,
                            Ada, Ned, Dee, Rena, J!@#$#$oel, Lora, Cecil, Aaron, Flora, Tina, Arden, 
                            Noel, and Ellen sinned.
                          """
        self.assertVector = isPalindrome(self.multi_line)
        self.assertEquals(self.assertVector, False)

    def test_multi_line_palindrome_punctuation(self):
        self.multi_line = """Dennis, Nel~@@@@@@l, Edna, Leon, Nedra, Ani~~~~ta, Rolf~~~, Nora,
                             Alice, Carol, Leo, Jane, Reed, Dena, D~~ale, Basil, Rae,
                            Penny, Lana, Dave, De!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~nny, 
                            Lena, Ida, Bernad!!!!!!~~ette, Ben, Ray, 
                            Lila, Nina, Jo, Ira, Mara, Sara, Mar!~~io, Jan, Ina, Lily, Arne,
                            Bette, Dan, Reba, Diane, Lynn, !"#$%&'()*+,-./:;<=>?@[\]^_`{Ed|}~, Eva, Dana, Lynne, Pearl, Isabel,
                            Ada, Ned, Dee, Rena, J!@#$#$oel, Lora, Cecil, Aaron, Flora, Tina, Arden, 
                            Noel, and Ellen sinned.
                          """
        self.assertVector = isPalindrome(self.multi_line)
        self.assertEquals(self.assertVector, True)



if __name__ == "__main__":
    unittest.main(verbosity=2)