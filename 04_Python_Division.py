"""
Program		:	"Python: Division"
Author		:	Ramesh K P
Language    :	Python
IDE		    :	Visual Studio
Date		:	24/08/2021
mail		:	rameshofficial75@gmail.com
Expected Input	:	First Line : Input the first integer
                    Second Line : Inout the second integer
Expected Output	:	First Line : Display the integer division of two numbers
                    Second Line : Display the float division of two numbers
"""

from __future__ import division
if __name__ == '__main__':
    print("\n")
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    print("Integer division of two numbers: " + str(first_number//second_number))
    print("Float division of two numbers: " + str(first_number/second_number))
    print("\n")