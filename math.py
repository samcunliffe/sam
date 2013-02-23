
def is_even(n):
  """Test integer n for even parity"""
  return n%2==0

def is_odd(n):
  """Test integer n for odd parity"""
  return not is_even(n)


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
