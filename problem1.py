#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""
import math
def hypotenuse(a,b,flag):
    if flag==True:
        c=math.sqrt(a**2+b**2)
        return c
    elif flag==False:
        if a>b:
            c=math.sqrt(a**2-b**2)
            return c
        elif b>a:
            c=math.sqrt(b**2-a**2)
            return c
