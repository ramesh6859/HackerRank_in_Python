"""
Program		:	"Print Function"
Author		:	Ramesh K P
Language    :	Python
IDE		    :	Visual Studio
Date		:	26/08/2021
mail		:	rameshofficial75@gmail.com
Expected Input	:	First Line : Input the number
Expected Output	:	First Line : Display the number from 1 to the 
                                 number
"""

import os
if __name__ == '__main__':
    os.system("clear")
    print("\n")
    input_number = int(input("Enter the number: "))
    for i in range(1, input_number + 1):
        print (i, end = ' ')
    print("\n")
