from numba import jit
import math

def function(x):
    return (math.sin(x)/x)

@jit(nopython=True)
def run(integral,itteration,lower_limit,dx):
    for p in range(1,itteration):
        try:
            integral = integral + (math.sin(lower_limit + p*dx)/(lower_limit + p*dx))*dx
        except:
            pass
    return integral
