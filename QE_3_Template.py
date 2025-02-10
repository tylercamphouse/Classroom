"""Author: Suresh
Program: Quadratic Equation Solver - Version 1.0
Description: A program to compute real and complex roots of a 
quadratic equation representing a parabola, using
if, elif, and else condition statements"""

"""Import the math functions pow and sqrt 
from the math module"""
from math import pow,sqrt

#Display the standard form of a quadratic equation
print("""The program computes the roots of 
            the quadratic equation:
            y = ax^2 + bx + c""")

#Prompt the use to input coefficients a, b, and c
a = float(input('Enter the value of the coefficient a: '))
b = float(input('Enter the value of the coefficient b: '))
c = float(input('Enter the value of constant c: '))

#Display the QE to be solved
"""Insert the + symbol before the data format type   
to force positive numbers to be displayed with the
positive sign."""
print('{0:.2f}x^2{1:+.2f}x{2:+.2f}'.format(a,b,c))

#Compute the denominator 2a of the roots
denom = 2*a
print('The value of the denominator: 2a = ',denom)

#Compute the discriminant of the roots
discriminant = pow(b,2.0) - 4.0*a*c
print('The value of the discriminant = ',discriminant)

"""Compute the roots using if, elif and else statements"""
#Check is the value of denom is close to zero
if denom < 0.0000001:#Small tolerance value
    print('The coefficient of x^2 is small')
elif discriminant > 0.0: #real roots exists
    x1 = (-b + sqrt(discriminant))/denom
    x2 = (-b - sqrt(discriminant))/denom
    #Display the computed roots. \t will insert a tab
    print('x1 = {0:.2f}\tx2 = {1:.2f}'.format(x1,x2))
elif discriminant < 0.0: #complex root exists
    x1 = complex((-b/denom),(sqrt(-discriminant)/denom))
    x2 = complex((-b/denom),(-sqrt(-discriminant)/denom))
    #Display the complex computed roots. \t will insert a tab
    print('x1 = {0:.2f}\tx2 = {1:.2f}'.format(x1,x2))
else:
    x1 = x2 = -b/denom
    #Display the computed repeared roots. \t will insert a tab
    print('x1 = {0:.2f}\tx2 = {1:.2f}'.format(x1,x2))