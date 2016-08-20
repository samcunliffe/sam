"""RooFit utility functions"""
__authors__ = ["Sam Cunliffe"]


def make_rooplot(list_of_plotable, x_variable, path_to_save_plot, nbins = 50, 
                 list_of_draw_options = None):
    """Makes a basic RooPlot of plotable objects (RooDataSets or RooPdfs)"""
  
    # declare the RooPlot object
    the_plot = x_variable.frame(nbins)

    if list_of_draw_options:
        if len(list_of_plotable) != len(list_of_draw_options):
            print("error: length mismatch with provided draw options")
            print("len(list_of_plotable):", len(list_of_plotable))
            print("len(list_of_draw_options):", len(list_of_draw_options))
            print("will draw without options")


    # plot things on
    for i, plotable_object in enumerate(list_of_plotable):
        if list_of_draw_options:
            plotable_object.plotOn(the_plot, list_of_draw_options[i])
        else:
            plotable_object.plotOn(the_plot)

    # declare root TCanvas and draw onto
    from ROOT import TCanvas
    canvas = TCanvas()
    the_plot.Draw()
    canvas.SaveAs(path_to_save_plot)

    # make rootfile
    path_to_save_rootfile = path_to_save_plot.replace(".eps", ".root")
    path_to_save_rootfile = path_to_save_rootfile.replace(".pdf", ".root")
    path_to_save_rootfile = path_to_save_rootfile.replace(".png", ".root")
    path_to_save_rootfile = path_to_save_rootfile.replace(".gif", ".root")
    from ROOT import TFile
    rootfile = TFile(path_to_save_rootfile, "RECREATE")
    rootfile.cd()
    the_plot.Write()
    rootfile.Close()

    return


def get_rds_from_file(file_name, rds_name = "transversity", file_mode = "READ"):
    """Gets RooDataSet out of TFile"""
    print(file_name)
    import ROOT as r
    f=r.TFile(file_name, file_mode)
    rds=r.RooDataSet()
    f.GetObject(rds_name, rds)
    # TODO: add some checks of the tree
    print("Got the RooDataSet called:",rds.GetName())
    print(" containing:",rds.numEntries(),"entries")
    print(" now call print method ")
    rds.Print()
    return (f, rds) # have to return file to 'hold' tree

def make_component_rooplot(pdf, list_of_components, dataset, x_variable,
                           path_to_save_plot, nbins = 50):
  """Makes a RooPlot of a pdf and its componets (after a fit?)"""

  import ROOT as r
  cmpt = r.RooFit.Components
  dash = r.RooFit.LineStyle(r.kDashed)
  colr = r.RooFit.LineColor
  colour_code = 5
  
  # declare the RooPlot object
  the_plot = x_variable.frame(nbins)

  # plot things on
  dataset.plotOn(the_plot)
  pdf.plotOn(the_plot)

  for component_pdf_name in list_of_components:
    print(component_pdf_name, colour_code)
    pdf.plotOn(the_plot, cmpt(component_pdf_name), dash, colr(colour_code))
    colour_code += 2

  dataset.plotOn(the_plot)

  # declare root TCanvas and draw onto
  canvas = r.TCanvas()
  the_plot.Draw()
  canvas.SaveAs(path_to_save_plot)

  # make rootfile
  path_to_save_rootfile = path_to_save_plot.replace(".eps", ".root")
  rootfile = r.TFile(path_to_save_rootfile, "RECREATE")
  rootfile.cd()
  the_plot.Write()
  rootfile.Close()

  return



def make_hists_rooplot(list_of_roodatahists, x_variable, path_to_save_plot, 
                       key_and_colors = None):
    """Makes a basic RooPlot of plotable objects (RooDataSets or RooPdfs)"""
  
    # declare the RooPlot object
    nbins = list_of_roodatahists[0].createHistogram("temp", x_variable).GetNbinsX()
    the_plot = x_variable.frame(nbins)

    # sanity check
    if key_and_colors:
        if len(list_of_roodatahists) != len(key_and_colors):
            print("error: length mismatch with provided draw options")
            print("len(list_of_roodatahists):", len(list_of_roodatahists))
            print("len(key_and_colors):", len(key_and_colors))
            print("will draw without key/legend")

    from ROOT import RooFit as rf
    from ROOT import TLegend
    legend = None

    # plot things on
    if key_and_colors:
        
        legend = TLegend()

        # plot the histos colorfully with legend
        for histo, key in zip(list_of_roodatahists, key_and_colors):
            legname, colorcode = key
            ma = rf.MarkerColor(colorcode)
            li = rf.LineColor(colorcode)
            histo.plotOn(the_plot, ma, li)
            legend.AddEntry(histo, legname)

    else:
        # or just plot them on
        for histo in list_of_roodatahists:
            histo.plotOn(the_plot)

    # declare root TCanvas and draw onto
    from ROOT import TCanvas
    canvas = TCanvas()
    the_plot.Draw()
    if legend:
        legend.Draw()
    canvas.SaveAs(path_to_save_plot)

    # make rootfile
    path_to_save_rootfile = path_to_save_plot.replace(".eps", ".root")
    path_to_save_rootfile = path_to_save_rootfile.replace(".pdf", ".root")
    path_to_save_rootfile = path_to_save_rootfile.replace(".png", ".root")
    path_to_save_rootfile = path_to_save_rootfile.replace(".gif", ".root")
    from ROOT import TFile
    rootfile = TFile(path_to_save_rootfile, "RECREATE")
    rootfile.cd()
    the_plot.Write()
    if legend:
        legend.Write()
    rootfile.Close()

    return


def make_parameters_text_file(fit_result, path_to_save_text_file):
  """Print the RooFitResult printed all nicely to the file 'pars.txt'"""

  # check the path makes sense and fix if nessicary
  if not path_to_save_text_file.endswith("/pars.txt"):  
    if path_to_save_text_file.endswith("/"):
      path_to_save_text_file += "pars.txt"
    else:
      path_to_save_text_file += "/pars.txt"
  print("saving parameters to:", path_to_save_text_file)

  # create output file
  from ROOT import std
  text_file = std.ofstream(path_to_save_text_file)

  # print the RooFitResult using the stupid cryptic options
  # see: http://root.cern.ch/root/html/src/RooFitResult.cxx.html#AjowS
  # for details
  fit_result.floatParsFinal().printMultiline(text_file, 1111, True)

  text_file.close()
  return

def get_wspace_from_file(file_name, wspace_name, dir_name = "", 
                         file_mode = "READ"):
  """Gets RooWorkspace out of TFile"""
  import ROOT as r
  f=r.TFile(file_name, "READ") #file_mode)
  w=r.RooWorkspace()
  f.GetObject(dir_name + wspace_name, w)
  # TODO: add some checks 
  print("Got the workspace called:", w.GetName())
  print("Print method:")
  w.Print()
  return (f,w) # have to return file to 'hold' tree


def make_roodataset(python_list_of_vars, file_name, 
                    tree_name = "BdToKstarMuMu_Data", 
                    path_to_save = "select_kstarmumu_roodataset.root"):
    """
    Makes a RooDataSet in the current directory. 
    I only really want to do this once since python is slow.
    """

    from ROOT import RooArgSet, RooDataSet

    # open the files and get the trees
    from utils.root import get_tree_from_file
    (f, t) = get_tree_from_file(file_name, tree_name)

    # get the variables into the stupid roofit format
    ras = RooArgSet()
    for var in python_list_of_vars:
        ras.add(var)
    ras.Print()

    # make a RooDataSet from both trees
    print("making the RooArgSet... yes this takes a long time because python"\
        + " is slower than C++ \nperhaps you could use the time to reflect"\
        + "on how much you hate coding C++ and how beautiful python is")
    ds = RooDataSet("ds", "data set", t, ras)
    print("made the RooDataSet")

    # save it
    from ROOT import TFile
    fds = TFile(path_to_save, "RECREATE")
    fds.cd()
    ds.Write()
    print("saved the RooDataSet")

    return ds


def add_histogram_to_canvas(canvas, variable, dataset, stupid_root_colour):
    from ROOT import RooArgList, RooFit#, std
    canvas.cd()
    root_histogram = variable.createHistogram("h")
    root_histogram.Rebin(3)
    dataset.fillHistogram(root_histogram, RooArgList(variable))
    root_histogram.Scale(1.0/root_histogram.GetEntries())
    root_histogram.GetYaxis().SetRangeUser(0, 0.1)
    root_histogram.SetMarkerColor(stupid_root_colour)
    root_histogram.SetLineColor(stupid_root_colour)
    root_histogram.Draw("same")

