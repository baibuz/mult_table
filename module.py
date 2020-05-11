import numpy as np
import sys
def isinteger(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

def check_command_line(arguments):
    if "help" in arguments:
        # print help message if asked
        print("The program outputs a multiplication table up to the input number. Usage: ")
        print("python3 %s N "%arguments[0])
        print("where N is a positive integer")
        sys.exit(0)
    else:
        if len(arguments)<2:
            # check if number provided
            print("Wrong input, see help:")
            print("python3 %s help "%arguments[0])
            sys.exit(0)

def readin_integer(arguments):
    check_command_line(arguments)
    N_input = arguments[1]
    #making sure N is integer
    try:
        N = int(N_input)
        if N > 1:
            return N
        else:
            print("N should be > 0")
            sys.exit(0)
    except ValueError:
        print("Input number N = %s is not an integer"%N_input)
        sys.exit(0)
def generate_mult_table(N):
    table = np.zeros((N, N), dtype=int)
    for i in range(N):
        for j in range(N):
            # assigning multiplication table
            table[i,j] = (i+1)*(j+1)
    return(table)