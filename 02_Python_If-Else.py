"""
Program		:	"Python If-Else"
Author		:	Ramesh K P
Language    :	Python
IDE		    :	Visual Studio
Date		:	23/08/2021
mail		:	rameshofficial75@gmail.com
Expected Input	:	First Line : Input the number
Expected Output	:	First Line : If the number is odd, print Weird.
                    If the number is even and in the inclusive range 
                    of 2 to 5, print Not Weird.
                    If the number is even and in the inclusive range 
                    of 6 to 20, print Weird.
                    If the number is even and greater than 20, print 
                    Not Weird
"""

import os
if __name__ == "__main__":
    os.system("clear")
    print("\n")
    input_number = int(input("Enter the number: "))
    if input_number%2 == 1:
        print("Weird")
    elif input_number%2 == 0 and (input_number >= 2 and input_number < 6):
        print("Not Weird")
    elif input_number%2 == 0 and (input_number >= 6 and input_number < 21):
        print("Weird")
    else:
        print("Not Weird")
    print("\n")