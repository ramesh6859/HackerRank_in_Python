"""
Program		:	"Loops"
Author		:	Ramesh K P
Language    :	Python
IDE		    :	Visual Studio
Date		:	24/08/2021
mail		:	rameshofficial75@gmail.com
Expected Input	:	First Line : Input the number
Expected Output	:	First Line : Display the square of the numbers 
                                 from 0 to the input number
"""

import os
if __name__ == '__main__':
    os.system("clear")
    print("\n")
    input_number = int(input("Enter the limit: "))
    for i in range(input_number):
        print("The square of the number {0:d} is {1:d}".format(i, i*i))
    print("\n")