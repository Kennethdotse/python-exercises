print("enter the co-efficients of the quadratic of general form ax^2+bx+c=0")
a= int(input("a = "))
b=int(input("b = "))
c= int(input("c = "))
import cmath #this enables you to perform complex functions
from math import sqrt #this enables you to take square root
x1 = (-b+cmath.sqrt(b**2 - 4*a*c ))/2*a
x2 = (-b-cmath.sqrt(b**2 - 4*a*c ))/2*a
print( "x1 = {}  x2 ={}".format(x1,x2))
x=cmath( float(input("x= ")))