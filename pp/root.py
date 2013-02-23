
import ROOT as r
def get_tree_from_file(file_name,tree_name="DecayTree",dir_name="B02JpsiPi0Tuple/"):
  """Gets TTree out of TFile"""
  f=r.TFile(ROOTFILES+file_name)
  t=r.TTree()
  f.GetObject(dir_name+tree_name,t)
  print "Got the tree called:",t.GetName()
  print " containing:",t.GetEntries(),"entries"
  return (f,t) # have to return file to 'hold' tree

