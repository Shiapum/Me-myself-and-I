#Print the following string in a specific format:
##"Twinkle, twinkle, little star, How I wonder what you are! 
##      Up above the world so high, Like a diamond in the sky. 
##          Twinkle, twinkle, little star, How I wonder what you are!"

print ("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

#Write a program to get the Python version
import sys
print ("Pyrthon version: ", sys.version)
print ("Version info:", sys.version_info)

#Wite a program to display current time
import time
print (time.ctime())

#Wite a program to display current time with "%Y-%m-%d %H:%M:%S" format
import datetime
current_time = datetime.datetime.now()
print (current_time.strftime("%Y-%m-%d %H:%M:%S"))

#Compute the area of a circle
import math
radius = float(input("Circle radius:"))
a = (math.pi * (radius**2))
print ("The area of circle is", a)

#Write a program that changes form "Name" "Last Name" to "Last Name" "Name"
x = str(input("Input your name:"))
y = str(input("Now input your last name:"))

y, x = x, y
print( "Hello", x , y,"!")

#Write a program to invert the name
name = str(input("Enter your Name"))

#[::-1] is a slice statement that means start at the end of the string and end at position 0 with the size of -1 step
name = name [::-1]  
print (name)

#Write a program which accepts a sequence of csv from user and generate a list and a tuplet
number = float(input("write 10 numbers sepatated by a comma"))
number_list = number.split(",")
number_tuple = tuple(number_list)



