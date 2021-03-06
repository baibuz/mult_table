# The program reads in an integer number from command line,
# creates a multiplication table,
# and prints it
# Requires pandas and numpy modules installed
# by E. baibuz

import sys,os
sys.path.append(os.getcwd())
import module
from module import *

#Reading command line arguments
N = readin_integer(sys.argv)
print("Multiplication table for N = %i"%N)
# main program starts here
table = generate_mult_table(N)

#Uncomment next line if pandas is unavailable 
#print(table)

#printing the table with pandas module
from pandas import DataFrame
df = DataFrame(table)
# print to a terminal
print(df.to_string(index = False, header=False))
