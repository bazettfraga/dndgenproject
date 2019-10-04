import random
import yaml
import sys
import fullrand
import userrand

while(1):
    a = int(input("Please select an option\n1. Fully random character\n2. User-defined randomness.\n3. Exit.\n"))

    if a == 1:
        print("\n")
        fullrand.genChar()
        print("\n")
    if a == 2:
        print("\n")
        userrand.userGenChar()
        print("\n")
    if a == 3:
        sys.exit()