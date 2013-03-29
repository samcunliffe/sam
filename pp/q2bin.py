"""A q2 bin class to deal with, for example K*mm binning scheme"""

class q2bin:
  """A single bin in q2, the dimuon invariant mass squared"""
  def __init__(self, low, high):

    # titles for plots in this bin
    self.simple_title = "%.2f to %.2f" % (low, high)
    self.latex_title = "(%.2f < q^{2} < %.2f)GeV^{2}/c^{4}" % (low, high)

    # cut formatted for the DaVinci tuple branch names
    # note that the LHCb units are MeV => MeV-squared
    q2_name  = "B0_qsquared"
    low_cut  = "(%s > %.2fe6)" % (q2_name, low)
    high_cut = "(%s < %.2fe6)" % (q2_name, high)
    self.cut = "%s && %s" % (low_cut, high_cut)

  def __str__(self):
    # gives a result of str() for this object allowing print command
    return "Instance of q2 bin class. Bin is %s" % (self.simple_title)

