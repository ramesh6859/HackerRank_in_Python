"""
Program		:	"Write a function"
Author		:	Ramesh K P
Language    :	Python
IDE		    :	Visual Studio
Date		:	26/08/2021
mail		:	rameshofficial75@gmail.com
Expected Input	:	First Line : Input the year
Expected Output	:	First Line : Display whether the year is leap 
                                 year or not
"""

#   Function declaration and definition
def is_leap(function_parameter_year):
    if  ((function_parameter_year % 400 == 0) or 
        (function_parameter_year % 100 != 0) and 
        (function_parameter_year % 4 == 0)):
        print("{0:d} is a Leap Year".format(function_parameter_year))
    else:
        print("{0:d} is not a Leap Year".format(function_parameter_year))

import os
#   Main function 
if __name__ == '__main__':
    os.system("clear")
    print("\n")
    input_year = int(input("Enter the year: "))
    is_leap(input_year)
    print("\n")
    