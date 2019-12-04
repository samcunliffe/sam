"""Statistics utility functions"""
__authors__ = ["Sam Cunliffe"]

import uncertainties as u
import math



def check_has_uncertainty(n):
  '''Checks the type of n to see if it's a number with uncertainty'''
  if type(n) == "uncertainties.Variable":
    return True
  else:
    return False



def counted(n):
  """A Poisson counted number with uncertainty sqrt(n)"""
  return u.ufloat((n, math.sqrt(n)))



