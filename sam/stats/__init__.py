
import uncertainties as u

def poisson_counted(n):
    """a poisson counted number with sqrt n error"""
    from math import sqrt
    return u.ufloat(n, sqrt(n))
