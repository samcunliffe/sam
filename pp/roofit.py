"""RooFit specific functions"""

def make_rooplot(list_of_plotable, x_variable, path_to_save_plot, nbins = 50):
  """Makes a basic RooPlot of plotable objects (RooDataSets or RooPdfs)"""
  
  # declare the RooPlot object
  the_plot = x_variable.frame(nbins)

  # plot things on
  for plotable_object in list_of_plotable:
    plotable_object.plotOn(the_plot)

  # declare root TCanvas and draw onto
  from ROOT import TCanvas
  canvas = TCanvas()
  the_plot.Draw()
  canvas.SaveAs(path_to_save_plot)
  return


  def make_parameter_plot(fit_result, path_to_save_plot):
    """Make a TCanvas plot containing the text of the RooFitResult"""

  from ROOT import RooPlot
  the_plot = RooPlot()
  fit_result.plotOn(the_plot)

  from ROOT import TCanvas
  canvas = TCanvas()
  the_plot.Draw()
  canvas.SaveAs(path_to_save_plot)
  return


def make_parameters_text_file(fit_result, path_to_save_text_file):
  """Print the RooFitResult printed all nicely to the file 'pars.txt'"""

  # check the path makes sense and fix if nessicary
  if not path_to_save_text_file.endswith("/pars.txt"):  
    if path_to_save_text_file.endswith("/"):
      path_to_save_text_file += "pars.txt"
    else:
      path_to_save_text_file += "/pars.txt"
  print "saving parameters to:", path_to_save_text_file

  # (re)create output file
  text_file = open(path_to_save_text_file, "w")

  # print the RooFitResult using the stupid cryptic options
  # see: http://root.cern.ch/root/html/src/RooFitResult.cxx.html#AjowS
  # for details
  fit_result.floatParsFinal().printMultiline(text_file, 1111, True)

  text_file.close()
  return

