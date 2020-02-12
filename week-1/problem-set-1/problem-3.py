# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the 
# letters occur in alphabetical order. For example, if 
# s = 'azcbobobegghakl', then your program should print
#   $Longest substring in alphabetical order is: beggh
#
# In the case of ties, print the first substring. For example, if 
# s = 'abcbcd', then your program should print
#   $longest substring in alphabetical order is: abc

s = 'azcbobobegghakl'
alphabet = "abcdefghijklmnopqrstuvwxyz"
substring = ""
longest_substring = ""
iter_alpha = None
for x in s:
    if(iter_alpha == None): #sets alphabet index to first letter if there is none set
        iter_alpha = alphabet.find(x)
        substring += x
        continue
    elif(alphabet.find(x) == iter_alpha): #if x is the same letter as the previous one, add it to the substring
        substring += x
        continue
    elif(alphabet.find(x) == iter_alpha + 1): #if x is one letter ahead in the alphabet, add it to the substring
        substring += x
        iter_alpha += 1 #move the alphabet iterator one letter forward
        continue
    else:###problem may be here
        print(substring + " :IS THE SUBSTRING")
        if(longest_substring == ""):
            longest_substring = substring
        if(longest_substring < substring):
            longest_substring = substring
        iter_alpha = None
        substring = ""
        print(longest_substring + " :IS THE LONGEST SUBSTRING")
    
print("Longest substring in alphabetical order is: %s"%longest_substring)

        

