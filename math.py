import math as m
import time as t

base_funct = input("What's the problem?  ").lower()



def run_mult():    
    no1 = float(input("What is the first number?  "))
    no2 = float(input("What is the second number?  "))
    
    answer = no1*no2

    print()
    print("The answer is", answer)
def run_div():
    no1 = float(input("What is the base number?  "))
    no2 = float(input("What are we dividing by?  "))

    answer = no1 / no2

    print()
    print("The quotient is", answer)
def run_sub():
    no1 = float(input("What is the base number?  "))
    no2 = float(input("What are we subtracting?  "))

    answer = no1 - no2

    print()
    print("The answer is", answer)
def run_add():
    no1 = float(input("What is the first number?  "))
    no2 = float(input("And the second?  "))

    answer = no1 + no2

    print()
    print("The sum is", answer)
def run_exp():
    no1 = float(input("What is the base number?  "))
    no2 = float(input("That's all fine and dandy but to the power of what?  "))

    answer = no1 ** no2
    
    print()
    print("The result is", answer)
def run_root():
    no1 = float(input("What is within the radical?  "))
    no2 = float(input("What is the exponent attached to the radical?  "))

    answer = no1 ** (1 / no2)

    print()
    print("The result is", answer)



if (base_funct == "multiply"):
    run_mult()
    print()
elif (base_funct == "divide"):
    run_div()
    print()
elif (base_funct == "subtract"):
    run_sub()
    print()
elif (base_funct == "add"):
    run_add()
    print()
elif (base_funct == "exponent"):
    run_exp()
    print()
elif (base_funct == "root"):
    run_root()
    print()
else:
    print()
    print("that is not yet a function")