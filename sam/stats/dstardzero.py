"""D*-D0 background
An emperical function to describe the D* D0 background turn on point
in charm mixing analyses. Egede et al.
http://root.cern.ch/root/html/src/RooDstD0BG.cxx.html
"""


from math import exp


def dstardzero(m, m0, c, a, b):
  """The D*-D0 background pdf"""
  arg   = float(m - m0)
  if arg <= 0: return 0
  ratio = float(m)/float(m0)
  part1 = (1 - exp(arg/c))*(ratio**a)
  part2 = b*(ratio - 1.0)
  return part1 + part2
