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
    
    print ("The area of triangle with sides {0}, {1}, {2} is: ".format(side_a,side_b,side_c,), '%0.2f' %area) 

    return 

def quadratic_equation ():
    """Formula to solve quadratic equations"""
    a = complex(input('a ='))
    b = complex(input('b ='))
    c = complex(input('c ='))

    if (a==0):
        print ("error")
    else:
        d = (b**2) -(4* a*c)
        x_1 = (-b + cmath.sqrt(d)) / (2*a)
        x_2 = (-b - cmath.sqrt(d)) / (2*a)
        print ('x_1 is {0} and x_2 is {1}'.format(x_1,x_2))
    
    return

Heron_formula()


