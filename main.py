import engine
import math


def main():

    lower_limit = -10000
    upper_limit = 10000

    dx = 10 ** (-5)

    itteration = math.ceil((upper_limit - lower_limit) / dx)
    integral = engine.run(0, itteration, lower_limit, dx)

    print("the value of the integral is: " + str(integral))


def test():

    lower_limit = -math.pi
    upper_limit = math.pi

    dx = 10 ** (-5)

    itteration = math.ceil((upper_limit - lower_limit) / dx)
    integral = engine.run(0, itteration, lower_limit, dx)

    print("the value of the integral is: " + str(integral))


main()
