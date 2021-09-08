# Python interprets anything after a # as a comment

# print() - output will be anything inside the ()
# Structure: print (value,sep=' ',end='\n', file=sys.stdout, flush=False)
import cmath

print("Hello World!")
print(5+5)
print("Hey","How are you?",sep='_',end='\n')

#identifiers cannot start with a digit,special symbols nor keywords. 
#keywords are reserved words like: True, False, else, of, def, del, global...
#for more keywords: https://www.programiz.com/python-programming/keyword-list
#python is case sensitive, so A and a are different

# Next is addition
num1 = 1
num2 = 2
sum = num1 + num2
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

# Adding user input
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
sum = float(num1) + float(num2)
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

# Using no variables
# To define a function inside the print $ can be used, then %(Function)
# %.1f 
print('The sum is %.1f' %(float(input('Enter first number: ')) + float(input('Enter second number: '))))

#Numeric literals
a = 0b1010  #Binary literal
b = 100     #Decimal literal
c = 0o310   #Octal literal
d = 0x12c   #Hexadecimal literal
#float literal
float_1 = 10.5
float_2 = 1.5e2

#Complex literal
x= 3.14j 
print (x.imag, x.real)

#literal collections in Python
fruits = ["apple", "mango", "banana"]  #list defined by []. List items are ordered, changeable, and allow duplicate values. 
number = (1, 2, 3) #tuple defined by (). Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
alphabet = {'a':'apple', 'b':"ball", 'c':"cat"} #dictionary defined by {a:b}. Dictionaries are used to store data values in key:value pairs. Dictionary items are ordered, changeable, and does not allow duplicates.
vowels = {'a', 'b', 'c', 'd', 'c'} #set is defined by {}. Sets are used to store multiple items in a single variable. Set items are unordered, unchangeable, and do not allow duplicate values.

