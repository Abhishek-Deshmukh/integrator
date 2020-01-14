from pprint import pprint
import engine
import math

def main():

    lower_limit = -3
    upper_limit = 3

    dx = 10**(-3)

    number_of_itterations = dx/(upper_limit-lower_limit)

    integral = 0
    itteration = math.ceil((upper_limit - lower_limit)/dx)
    integral = engine.run(integral,dx,upper_limit,lower_limit)

    pprint("the value of the integral is: " + str(integral))
