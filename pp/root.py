"""Root specific functions"""

def get_tree_from_file(file_name, tree_name="DecayTree",
                       dir_name="", file_mode="READ"):
  """Gets TTree out of TFile"""
  import ROOT as r
  f=r.TFile(file_name, file_mode)
  t=r.TTree()
  f.GetObject(dir_name + tree_name, t)
  print "Got the tree called:",t.GetName()
  print " containing:",t.GetEntries(),"entries"
  return (f,t) # have to return file to 'hold' tree
