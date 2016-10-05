from math import sqrt

def counted_ratio_error(n, N):
    return sqrt(n*(N-n) /(N*N*N))

def efficiency_divide(hn, hN):
    """Make an efficiency ratio from a subsample n selected from N)"""
    # TODO: add a check that the histograms given in are identical binning etc
    hR = hn.Clone()
    for bin_ in range(hn.GetNbinsX()):
        n = hn.GetBinContent(bin_)
        N = hN.GetBinContent(bin_)
        if N!=0:
            R = n/N
            dR = counted_ratio_error(n, N)
        else:
            print('error dividing by zero at bin #%i' % bin_)
            R = 0
            dR = 0
        hR.SetBinContent(bin_, R)
        hR.SetBinError(bin_, dR)
    hR.SetMinimum(0)
    hR.SetMaximum(1.01) # aesthetic purposes
    return hR
        


