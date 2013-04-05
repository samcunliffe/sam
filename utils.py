"""Miscellaneous useful functions"""


def lensort(list_of_objects_with_length):
  """Sorts list objects by len"""
  return sort(list_of_objects_with_length, key=len)


def mkdir_p(directory):
  """Performs the equivalent of bash shell mkdir -p"""
  import os, errno
  try:
    os.makedirs(directory)
  except OSError as exc: # Python >2.5
    if exc.errno == errno.EEXIST:
      pass
  #else: raise
