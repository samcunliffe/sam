"""RooFit specific functions"""

def make_rooplot(list_of_plotable, x_variable, path_to_save_plot):
  """Makes a RooPlot of some plotable objects (RooDataSets or RooPdfs)"""
  p = x_variable.frame()
  for plotable_object in list_of_plotable:
    plotable_object.plotOn(p)
  from ROOT import TCanvas
  c=TCanvas()
  p.Draw()
  c.SaveAs(path_to_save_plot)
