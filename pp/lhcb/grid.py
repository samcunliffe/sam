"""LHCb Grid job diagnostic functions, calculate efficiency and luminosities"""

# TODO : Add the functions which either grep or search stdout files for a given
#        job directory preferably by working out the path to jobs output from 




def get_path_to_jobs():
  """Figures out the path to my jobs output depending on the host name"""
  import socket
  if socket.gethostname().endswith("hep.ph.ic.ac.uk"):
    # on an Imperial College HEP machine
    return "/vols/lhcbdisk04/scunliffe/gangadir/workspace/stc09/LocalXML/"
  elif socket.gethostname().endswith("cern.ch"):
    # on a CERN machine
    return "/afs/cern.ch/work/s/scunliff/gangadir/workspace/scunliff/LocalXML/"
  else:
    print "get_path_to_jobs ERROR: not on a recognised host"
    return "ERROR"



def cd_to_job_dir(n):
  """Change working directory to job output"""
  print "cd_to_job_dir(%i)" %n
  import os.system
  joboutput = get_path_to_jobs()
  system("cd %s/%i" % (joboutput, n))
  return



def check_all_dirs_have_rootfiles(n, rootfile_name = "*.root"):
  """Checks that there are no missing subdirs and each have a .root file"""
  print "check_all_dirs_have_rootfiles(%i)" % n

  # get list of numeric dirs
  from os import listdir as ls
  list_of_subdir_numbers = [int(sdir) for sdir in ls('.') if sdir.isdigit()]

  # check there are no missing subdir numbers
  consecutive_numbers = range(max(list_of_subdir_numbers) + 1)
  list_of_subdir_numbers.sort()
  if consecutive_numbers != list_of_subdir_numbers:
    print "There seems to be a problem with a subjob directory missing"
    return False

  # check the presence of a rootfile
  for sdir in list_of_subdir_numbers:
    subdir_files = ls("%i/output/%s" % (sdir, rootfile_name))
    if not len(subdir_files):
      print "Subdirectoy %i does not have a rootfile" % sdir
      return False

  return True



def check_job(n):
  """Checks various sensible things"""
  print "check_job(%i)" % n
  return check_all_dirs_have_rootfiles(n)



def hadd_job(n, output_file_name):
  """Performs the hadd command"""
  import os
  os.system("hadd output/%s */output/*.root" % output_file_name)
  return



def check_and_hadd_job(n):
  """Run all functions in order"""
  print "check_and_hadd_job(%i)" % n
  from sam.pp.root import check_root_version
  if check_root_version(): 
    cd_to_job_dir(n)
    if check_job(n):
      #hadd_job(n)
      return 0
  return 0



def mc_job_selection_efficiency(DecProdEff,DecProdEffErr,nSelected,nRunOver):
  """Calculate the selection efficiency for a MC job"""
  from uncertainties import ufloat as u
  from math import sqrt as s
  e_dpc = u((DecProdEff,DecProdEffErr))
  nsel  = u((nSelected,s(nSelected)))
  nrun  = u((nRunOver,s(nRunOver)))
  out   = e_dpc*nsel/nrun
  print "(", 100*out, ") %"
  return out



def data_job_retention(nSelected,nRunOver):
  """Calculate the retention for a data job"""
  from uncertainties import ufloat as u
  from math import sqrt as s
  nsel  = u((nSelected,s(nSelected)))
  nrun  = u((nRunOver,s(nRunOver)))
  out   = nsel/nrun
  print "(", 100*out, ") %"
  return out
