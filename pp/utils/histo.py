"""Histogram utility functions"""

def integer_binning(start, stop):
    nints = stop - start
    return (nints+1, start-0.5, stop+0.5)


def normalise(histo):
    histo.Scale(1.0/histo.Integral())
    return histo


def scale_to_largest(firstplot, secondplot):
    """fix root annoyance, increase axis first"""
    max_first, max_second = firstplot.GetMaximum(), secondplot.GetMaximum()
    if max_first < max_second:
        delta = 0.05*(max_second-firstplot.GetMinimum()) # a bit for aesthetics
        firstplot.SetMaximum(max_second+delta)
    return firstplot, secondplot
