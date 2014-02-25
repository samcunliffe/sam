"""Generic useful functions in here."""

__authors__ = ["Alex Shires", "Kostas Petridis", "Sam Cunliffe"]
__date__ = "April 2013"

import os, sys

def turn_off_popup_plots():
    """Makes gROOT not spit out plot windows for every draw command"""
    from ROOT import gROOT
    gROOT.SetBatch(True)
    print "have set batch mode so you won't see popup plots"



def load_kstarll_libs():
  """Global gROOT command that loads RooRelBreitWigner and friends"""
  from ROOT import gSystem
  gSystem.Load("libRooFit.so")
  gSystem.Load("libPhysics.so")
  gSystem.Load("cpp/lib/libKstarLL.so") 
  ## relies on the ../lib directory having been made



def ssum(list_of_strings):
  """Sum the strings in a list of strings"""
  out = ""
  for string in list_of_strings:
    out += string
  return out



def run_cmd(cmd, test = False) :
    """wrapper for os.system to run bash command"""
    print cmd
    if not test :
        result = os.system(cmd) 
        if result < 0 :
            print "failed", result
            sys.exit(result)


def mkdir(dirname):
    run_cmd("mkdir " + dirname)

def mkdir_p(dirname):
    run_cmd("mkdir -p " + dirname)

def list2dictkeys(l):
    """returns a dictionary where the keys are the list items"""
    out = {}
    for listitem in l:
        out.update( {listitem: ""} )
    return out

