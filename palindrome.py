#write a python program to read a string as an input and check given string is palindrome or not
str=(input())

reverse=str[::-1]
if reverse==str:
    print(reverse,"is a palindrome")
else:
    print(reverse,"is not palindrome")    




