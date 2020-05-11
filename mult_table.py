import sys,os
sys.path.append(os.getcwd())
import module
from module import *
if "help" in sys.argv:
    print("The program outputs a multiplication table up to the input number. Usage: ")
    print("python %s N"%sys.argv[0])
    print("where N is an integer number")
else:
    if len(sys.argv)<2:
        print("Wrong input, see help:")
        print("python %s help "%sys.argv[0])
        exit
    else:
        N_input = sys.argv[1]
        if if_integer(N_input):
            N = int(N_input)
            print("Multiplication table for N = %i"%N)
        else:
            print("Input number N = %s is not an integer"%N_input)
            