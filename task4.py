#! python3
"""
Create a function called isInteger()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)
"""
def isInteger(number):
    #input:float
    #return value:true if the number is an integer;false otherwise
    if number%1==0:
        flag=True
        return flag
    else:
        flag=False
        return flag
