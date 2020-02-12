#
# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' 
# occurs in s. For example, if s = 'azcbobobegghakl', then your 
# program should print
# Number of times bob occurs is: 2
#


s = 'bokrbbobobobboobgofboboboboboyc'


bob = "bob"
startindex = 0
firstbob = True
count = 0

for times in range(len(s)-2): #loops enough times so every starting index can be checked for "bob"
    #print(s[startindex:]) #prints out the string from starting index
    #print(s[startindex:].find(bob)) #finds the first occourence of bob in the string
    if(startindex > len(s)-2):
        break
    
    if(firstbob == True):
        if(s[startindex:].find(bob) == 0):
            count += 1
            startindex += 1
            firstbob = False

    if(len(s) < 3):
        break
    
    # if(s[startindex:].find(bob) == 0)
        count += 1
        startindex += 1
    elif(s[startindex:].find(bob) != -1):
        startindex += s[startindex:].find(bob)
print("Number of times bob occurs is: %d"%count)
    

    
        