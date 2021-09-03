import cmath

# Python program to find the area of triangle
def Heron_formula ():
    """Heron's formula givesthe area of triangle when the length of all three sides are known"""
    
    side_a = float(input('Side a:'))
    side_b = float(input('Side b:'))
    side_c = float(input('Side c:'))

    
    #calculate semi-perimeter
    s= (side_a + side_b + side_c ) / 2
    
    #calculate area using Heron's formula
    area = (s* (s- side_a)* (s- side_b)* (s- side_c)) ** 0.5
    
    print ("The area of triangle with sides {0}, {1}, {2} is: ".format(side_a,side_b,side_c,), '%0.01f' %area) 

    return 

Heron_formula()