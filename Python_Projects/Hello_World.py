# Python interprets anything after a # as a comment

# print() - output will be anything inside the ()
# Structure: print (value,sep=' ',end='\n', file=sys.stdout, flush=False)

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

