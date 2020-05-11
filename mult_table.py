# The program reads in an integer number from command line,
# creates a multiplication table,
# and prints it
# Requires pandas and numpy modules installed
# by E. baibuz

import sys,os
sys.path.append(os.getcwd())
import module
from module import *
import numpy as np

#Reading command line arguments
if "help" in sys.argv:
    # print help message if asked
    print("The program outputs a multiplication table up to the input number. Usage: ")
    print("python3 %s N "%sys.argv[0])
    print("where N is an integer number")
    sys.exit(0)
else:
    if len(sys.argv)<2:
        # check if number provided
        print("Wrong input, see help:")
        print("python3 %s help "%sys.argv[0])
        sys.exit(0)
    else:
        N_input = sys.argv[1]
        #making sure N is integer
        if if_integer(N_input):
            N = int(N_input)
            print("Multiplication table for N = %i"%N)
        else:
            print("Input number N = %s is not an integer"%N_input)
            sys.exit(0)

# main program starts here
table = np.zeros((N, N), dtype=int)
for i in range(N):
    for j in range(N):
        # assigning multiplication table
        table[i,j] = (i+1)*(j+1)

#printing the table with pandas module
import pandas
df = pandas.DataFrame(table)
# print to a terminal
print(df.to_string(index = False, header=False))
