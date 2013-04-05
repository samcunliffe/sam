"""Some statistical functions"""

def weighted_average(list_of_values, list_of_weights):
  """The weighted average of list_of_values using weights in list_of_weights"""

  # check lengths match
  if len(list_of_values) != len(list_of_weights): return -1

  # do sum, could probably use a list comprehension here to be more pythonic
  for i in range(len(list_of_values)): 
    out += list_of_values[i]*list_of_weights[i]
  return out
