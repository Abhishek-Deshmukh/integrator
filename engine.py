from numba import jit
import math


@jit(nopython=True)
def run(integral, itteration, lower_limit, dx):
    for p in range(1, itteration):
        try:
            x = lower_limit + p * dx
            # enter you function here
            function_at_x = math.sin(x) / x

            # do not touch if you don't know what you are doing
            integral = integral + function_at_x * dx
        except:
            print("didn't work")
    return integral
