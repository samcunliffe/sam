"""Root specific functions"""
__authors__ = ["Sam Cunliffe"]



def turn_off_popup_plots():
    """Turns pyROOT to batch mode (no popup plots)"""
    from ROOT import gROOT
    gROOT.SetBatch(True)
    return




def check_root_version():
    """Checks that the ROOT version is recent and decent"""
    from ROOT import gROOT
    print("utils.check_root_version: ROOT version: %s" % gROOT.GetVersion())
    ## could easily flag up untrusted versions with complex checking in here
    return (gROOT.GetVersionInt() > 53408)



def get_tree(tree_name, file, dir_name=''):
    import ROOT as r
    t=r.TTree()
    file.GetObject(dir_name + tree_name, t)
    print("Got the tree called: %s" % t.GetName())
    print(" containing: %i entries" % t.GetEntries())
    return (file,t) # have to return file to 'hold' tree




def get_tree_from_file(file_name, tree_name = "DecayTree",
                       dir_name = "", file_mode = "READ"):
    """Gets TTree out of TFile"""
    print(file_name)
    import ROOT as r
    f=r.TFile(file_name, file_mode)
    t=r.TTree()
    f.GetObject(dir_name + tree_name, t)
    print("Got the tree called: %s" % t.GetName())
    print(" containing: %i entries" % t.GetEntries())
    return (f,t) # have to return file to 'hold' tree




def get_trees_from_file(file_name, list_of_tree_names,
                       dir_name = "", file_mode = "READ"):
    """Gets TTree out of TFile"""
    print(file_name)
    import ROOT as r
    f=r.TFile(file_name, file_mode)
    t = []
    for name in list_of_tree_names:
        tr=r.TTree()
        f.GetObject(dir_name + name, tr)
        print("Got the tree called: %s" % tr.GetName())
        print(" containing: %i entries" % tr.GetEntries())
        t.append(tr)
    return (f,t)




def get_from_file(filename, tobjectname):
    """Gets a TObject from a TFile"""
    from ROOT import TFile
    fi = TFile(filename, "READ")
    to = fi.Get(tobjectname)
    return (fi, to)





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


def fit_gaussian(graph, verbose = False):
    """Fits a gaussian to a graph, using the simple ROOT Fit interface"""

    # function
    from ROOT import TF1
    f = TF1("fit_" + graph.GetName(), "gaus")
    if verbose:
        print("will fit with verbose \n\n")
        opt = "V"
    else: 
        opt = ""

    # do fit
    graph.Fit(f, opt)

    m = f.GetParameter(1) # mean
    dm = f.GetParError(1) # uncertainty on mean
    s = f.GetParameter(2) # sigma
    ds = f.GetParError(2) # sigma
    return (m, dm, s, ds)


def fit_double_gaussian(graph, verbose = False):
    """Fits a double gaussian to graph, using the simple ROOT Fit interface"""

    # function
    from ROOT import TF1
    first  = "[0]*exp(-0.5*((x-[1])/[2])**2)"
    second = "[3]*exp(-0.5*((x-[1])/[4])**2)"
    double = first + '+' + second
    f = TF1("fit_" + graph.GetName(), double)
    f.SetParNames('n1', 'mean', 'sigma1', 'n2', 'sigma2')
    f.SetParameters(0.7*graph.GetEntries(), 0, 0.006, .3*graph.GetEntries(), 0.004) 
    if verbose:
        print("will fit with verbose \n\n")
        opt = "V"
    else: 
        opt = ""

    # do fit
    graph.Fit(f, opt)

    #f12 = f.GetParameter(0) # fraction f12
    #df12 = f.GetParError(0) #
    m = f.GetParameter(1) # mean
    dm = f.GetParError(1) # uncertainty on mean
    s1 = f.GetParameter(2) # sigma_1
    ds1 = f.GetParError(2) # 
    s2 = f.GetParameter(4) # sigma_2
    ds2 = f.GetParError(4) #
    return (m, dm, s1, ds1, s2, ds2)

def fit_straight_line(graph, verbose = False):
    """Fits a straight line to a graph, using the simple ROOT Fit interface"""

    # function
    from ROOT import TF1
    f = TF1("fit_" + graph.GetName(), "pol1")
    if verbose:
        print("will fit with verbose \n\n")
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
        print("will fit with verbose \n\n")
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
