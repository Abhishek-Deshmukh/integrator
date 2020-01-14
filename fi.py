from pprint import pprint
import engine
import math

def main():

    lower_limit = -10000
    upper_limit = 10000

    dx = 10**(-5)

    integral = 0
    itteration = math.ceil((upper_limit - lower_limit)/dx)
    integral = engine.run(integral,itteration,lower_limit,dx)

    pprint("the value of the integral is: " + str(integral))
