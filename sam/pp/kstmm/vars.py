
"""A class to encompass the notion of a 'variable'. And usefull collections of 
variables i.e. the set of 'interesting' angular variables. This will simplify 
looping over them"""

__author__ = "Sam Cunliffe"
__email__ = "stc09@ic.ac.uk"


class Variable:
    """A single variable"""
    def __init__(self, name, title, binningscheme, units, branchname="NAME"):

        # unpack all arguments, set members
        self.name = name
        self.title = title
        self.nbins, self.low, self.high = binningscheme
        self.units = units
        if branchname == "NAME":
            self.branchname = self.name
        else:
            self.branchname = branchname
        return

    def __str__(self):
        # allows us to do print and str() on this object
        return "Instance of Variable class: ", self.name

    def tree_draw_cmd(self, histoname, includeBinning = False):
        """Generate the draw command on a tree"""
        if includeBinning:
            return "%s>>%s(%s,%s,%s)" % (self.branchname, histoname,
                                         self.nbins, self.low, self.high)
        else:
            return "%s>>%s" % (self.branchname, histoname)

    def make_quick_distribution(self, tree):
        """Just make a really quick plot of this variable on the tree
        I.e. to check that the branch exists and that binning is sensible"""
        import ROOT as r
        histoname = "h" + self.name
        h = r.TH1D(histoname, histoname, self.nbins, self.low, self.high)
        tree.Draw(self.tree_draw_cmd(histoname))
        c = r.TCanvas()
        h.Draw()
        c.SaveAs("quick_distribution_of_" + self.name + ".png")
        return

    def xaxis_label(self):
        """Makes a nicely formatted x axis label"""
        if self.units:
            return self.title + " (" + self.units + ")"
        else:
            return self.title

    #def get_roorealvar(self):
    #    """Create a RooRealVar for this guy"""
    #    import ROOT as r



mkpi   = Variable("mkpi", "m_{K#pi}", (50, 633, 1200), "MeV/c^{2}", "Kstar_M")
ctk    = Variable("ctk", "cos#theta_{K}", (100, -1.0, 1.0), "")
mkpimm = Variable("mkpimm", "m_{K#pi#mu#mu}", (50, 5180, 5780), "MeV/c^{2}", "B0_MM")
qsq    = Variable("qsq", "q^{2}", (100, 0.0, 19), "GeV^{2}/c^{4}")

angular_variables = [
    Variable("psq", "p^{2}", (100, 0.4, 1.25), "GeV^{2}/c^{4}"),
    Variable("mmumu", "m_{#mu#mu}", (100, 0.0, 4359), "MeV/c^{2}", "Jpsi_M"),
    Variable("ctl", "cos#theta_{l}", (100, -1.0, 1.0), ""),
    Variable("phi", "#phi", (50, -3.14, 3.14), "rad", "phi"),
    qsq,ctk,mkpi
]
