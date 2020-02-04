#
# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels 
# contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', 
# and 'u'. For example, if s = 'azcbobobegghakl', your program should 
# print:
# Number of vowels: 5
# 


s = 'aaabbbcabcdo'
vowels = ['a','e','i','o','u']
numOfVowels = 0

for letter in s:
    for vowel in vowels:
        if letter == vowel:
            numOfVowels += 1
print("Number of vowels: %d"%numOfVowels)