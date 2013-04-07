"""Usefull math functions that aren't in 'math'."""

def is_even(n):
  """Test integer n for even parity"""
  return n%2==0

def is_odd(n):
  """Test integer n for odd parity"""
  return not is_even(n)

def sum_of_squares(l):
  """Sum of sqares of all entries in list"""
  return sum([i*i for i in l])


def freq_of_list(l,entry_title="entry"):
  """Reports the frequency that entries occur in a list l"""
  d={}
  for entry in set(l):
    d.update({entry:l.count(entry)})
  
  print entry_title+"\t"+"frequency"
  print "-----------------------------"
  for entry in d:
    print entry,
    print "\t",
    print d[entry]

  return d
