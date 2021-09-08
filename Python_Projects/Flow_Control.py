#prints
import cmath
print ('This sentence is output to the screen')

a = 5
print ('The value of a is', a)

print (1, 2, 3, "a", "b", "c", sep='XDXD', end='n')

print ('I love {0} and {1}'.format('bread','butter'))
print ('I love {1} and {0}'.format('bread','butter'))

print ('Hello {name}, {greeting}'.format(greeting = 'how are you?', name = 'Miriam'))

x = cmath.pi*100
print ('The value of x is %0.2f' %x)

#Program to find the sum of all numbers stored in a list

#Lists of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

#variable to store the sum
sum = 0

#iterate over the list
for val in numbers: 
    sum = sum+val

print("The sum is:", sum)

#iterate through a list using indexing
genre = [ 'pop', 'rock' , 'jazz']

#iterate over the list using index
for i in range(len(genre)):
    print("I like", genre[i])

digits = [0, 1, 5]
for i in digits:
    print (i)
else:
    print("No items left")


