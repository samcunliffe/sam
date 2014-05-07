"""Root specific functions"""
__authors__ = ["Sam Cunliffe"]

def check_root_version():
    """Checks that the ROOT version is recent and decent"""
    from ROOT import gROOT
    print "utils.check_root_version: ROOT version:", gROOT.GetVersion()
    ## could easily flag up untrusted versions with complex checking in here
    return (gROOT.GetVersionInt() > 53408)

def get_tree_from_file(file_name, tree_name = "DecayTree",
                       dir_name = "", file_mode = "READ"):
    """Gets TTree out of TFile"""
    print file_name
    import ROOT as r
    f=r.TFile(file_name, file_mode)
    t=r.TTree()
    f.GetObject(dir_name + tree_name, t)
    # TODO: add some checks of the tree
    print "Got the tree called:",t.GetName()
    print " containing:",t.GetEntries(),"entries"
    return (f,t) # have to return file to 'hold' tree




def branch_exists(branch_name, tree):
    """Checks to see if a branch is in the tree"""
    if tree.GetBranch(branch_name):
        return True
    else:
        return False



def save_writable(list_of_writable_objects, path_to_save):
    """Saves a list of writable (T)objects to a .root file"""

    # check file name
    if not path_to_save.endswith(".root"):
        path_to_save += ".root"

    # new root file
    from ROOT import TFile
    f = TFile(path_to_save, "RECREATE")
    f.cd()

    # write all
    for writable_object in list_of_writable_objects:
        writable_object.Write()
        f.Close()
        return



def save_plot(plot, path_to_save, drawopt = "", xaxisname = None, 
              save_as_root = True):
    """Draws a plot to a TCanvas and saves as a root file"""

    # new canvas
    from ROOT import TCanvas
    c = TCanvas()
    c.cd()

    # axis might already be labelled use nonetype test
    if xaxisname:
        plot.SetXTitle(xaxisname)

    # draw and save in given file format
    plot.Draw(drawopt)
    c.SaveAs(path_to_save)

    # save as dot-root file
    path_for_rootfile = path_to_save.replace(".pdf", ".root")
    path_for_rootfile = path_for_rootfile.replace(".png", ".root")
    path_for_rootfile = path_for_rootfile.replace(".eps", ".root")
    if save_as_root: save_writable([plot], path_for_rootfile)
    return



def make_tgraph(xvals, yvals, yerrs = None, xerrs = None):
    """Makes a TGraph(Errors) from python lists of values"""
    from ROOT import TGraphErrors
    graph = TGraphErrors(len(xvals))

    # if we don't have errors provided then set them to zero
    if yerrs == None:
        yerrs = [0.0]*len(xvals)
        if xerrs == None:
            xerrs = [0.0]*len(xvals)

    # loop over and fill graph
    for i, (x,y, xerr, yerr) in enumerate(zip(xvals, yvals, xerrs, yerrs)):
        graph.SetPoint(i, x, y)
        graph.SetPointError(i, xerr, yerr)

    return graph




def fit_straight_line(graph, verbose = False):
    """Fits a straight line to a graph, using the simple ROOT Fit interface"""

    # function
    from ROOT import TF1
    f = TF1("fit_" + graph.GetName(), "pol1")
    if verbose:
        print "will fit with verbose \n\n"
        opt = "V"
    else: 
        opt = ""

    # do fit
    graph.Fit(f, opt)

    # y = mx + c   --->  pol1 = [0] + [1]*x
    c = f.GetParameter(0) # intercept
    m = f.GetParameter(1) # gradient
    return (c, m)


def fit_exponential(graph, verbose = False):
    """Fits a straight line to a graph, using the simple ROOT Fit interface"""

    # function
    from ROOT import TF1
    f = TF1("fit_" + graph.GetName(), "expo")
    if verbose:
        print "will fit with verbose \n\n"
        opt = "V"
    else: 
        opt = ""

    # do fit
    graph.Fit(f, opt)

    # 
    c = f.GetParameter(0) # intercept
    m = f.GetParameter(1) # gradient
    return (c, m)



def get_plots(filename):
    """opens a root file and returns a list of all plots"""
    plots = [] # will be the output
    plot_types = ['TH1D', 'TH2D', 'TH1F', 'TH2F', 'TGraph', 'TGraphErrors', 
                  'TGraphAsymErrors', 'RooPlot'] # can add to this
    from ROOT import TFile
    f = TFile(filename, "READ")
    file_contents = f.GetListOfKeys()
    for thing in file_contents:
        if thing.GetClassName() in plot_types: 
            # then the TObject is a plot
            plots += [thing.ReadObj()]
    return (f,plots)
