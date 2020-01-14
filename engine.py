from numba import jit

@jit(nopython=True)
def run(integral,dx,upper_limit,lower_limit):
    for p in range(1,itteration):
        integral = integral + ((lower_limit + p*dx)**2)*dx
    return integral
