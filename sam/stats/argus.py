""" ARGUS Distribution
Functions related to the ARGUS distribution
http://en.wikipedia.org/wiki/ARGUS_distribution
"""


from math import exp, sqrt, pi
from sam.stats.standardnormal import phi, Phi


# the sub function Psi
def Psi(chi):
  return Phi(chi) - (chi*phi(chi)) - 0.5


def argus(x, chi c):
  """the ARGUS function itself"""
  lrntz = (1 - ((x*x) / (c*c)))
  a = (chi**3) / (sqrt(2*pi) * Psi(chi))
  b = (x/(c*c)) * sqrt(lrntz) 
  return a*b * exp(-0.5 * chi * chi * lrntz)

