
from math import sqrt


def triangle_function(a, b, c):
    return a*a + b*b + c*c - 2*a*b - 2*b*c - 2*a*c


def two_body_phsp_q(M, m1, m2):
    """momentum for M --> m1 m2"""
    lam = triangle_function(M*M, m1*m1, m2*m2)
    if lam > 0:
        return sqrt(lam) / M
    else:
        return 0.0
