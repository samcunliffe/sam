"""LHCb Grid job diagnostic functions, calculate efficiency and luminosities"""

# TODO : Add the functions which either grep or search stdout files for a given
#        job directory preferably by working out the path to jobs output from 

import uncertainties as u

def get_path_to_jobs():
  """Figures out the path to my jobs output depending on the host name"""
  import socket
  if socket.gethostname().endswith("hep.ph.ic.ac.uk"):
    # on an Imperial College HEP machine
    return "/vols/lhcbdisk04/scunliffe/gangadir/workspace/stc09/LocalXML/"
  elif socket.gethostname().endswith("cern.ch"):
    # on a CERN machine
    return "/afs/cern.ch/work/s/scunliff/gangadir/workspace/scunliff/LocalXML/"
  else
    print "get_path_to_jobs ERROR: not on a recognised host"
    return "ERROR"

def mc_job_selection_efficiency(DecProdEff,DecProdEffErr,nSelected,nRunOver):
  """Calculate the selection efficiency for a MC job"""
  from math import sqrt as s
  e_dpc = u.ufloat((DecProdEff,DecProdEffErr))
  nsel  = u.ufloat((nSelected,s(nSelected)))
  nrun  = u.ufloat((nRunOver,s(nRunOver)))
  out   = e_dpc*nsel/nrun
  print "(", 100*out, ") %"
  return out

def data_job_retention(nSelected,nRunOver):
  """Calculate the retention for a data job"""
  from math import sqrt as s
  nsel  = u.ufloat((nSelected,s(nSelected)))
  nrun  = u.ufloat((nRunOver,s(nRunOver)))
  out   = nsel/nrun
  print "(", 100*out, ") %"
  return out
