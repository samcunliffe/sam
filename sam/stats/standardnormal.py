""" Standard Normal Distribution
Functions related to the Standard Normal Distribution 
http://en.wikipedia.org/wiki/Standard_normal#Definition
"""

from math import pi, sqrt, exp


def phi(x):
  """the pdf of the standard normal distribution (lowercase phi)"""
  return (1. / (2.*pi)) * exp(-0.5*x*x)

# the error function erf
from scipy.special import erf 


def Phi(x):
  """the cdf of the standard normal distribution (capital Phi)"""
  return 0.5 * (1.0 + erf(x/sqrt(2)))
