
"""graphmanip helper functions for TGraph, TGraphErrors or TGraphAsymErrors"""

from ROOT import TGraph, TGraphErrors, TGraphAsymmErrors

def remove_all_zeroes(li):
    """remove all zeros from a python list"""
    return filter(lambda a: a!=0, li)


def remove_zero_points(tgraph, asym=True):
    """remove zero points from a hadd-ed TGraph"""
    # do it the dumbass way by looping because TGraph is a cock 
    # and doesn't want to play nicely with numpy arrays
    size, newsize, nonzeros = tgraph.GetN(), 0, []
    from ROOT import Double as PassByRef
    for point in range(size):
        # unpack point with a pass-by-reference method because C++ sucks
        # I mean seriously should the OUTPUT of a function be passed IN
        x, y = PassByRef(0), PassByRef(0) 
        tgraph.GetPoint(point, x, y)
        if x > 0.000 or y > 0.000:
            newsize += 1          # size of new TGraphErrors
            nonzeros += [ point ] # point numbers for nonzero points

    # now prepare new TGraphErrors
    if asym:
        newtgraph = TGraphAsymmErrors(newsize)
    else:
        newtgraph = TGraphErrors(newsize)

    # now fill new TGraph
    for newpoint, oldpoint in enumerate(nonzeros):
        #print newpoint, oldpoint
        x, y = PassByRef(0), PassByRef(0)
        tgraph.GetPoint(oldpoint, x, y)
        newtgraph.SetPoint(newpoint, x.real, y.real)
        # errors don't need pass-by-ref because why bother being consistent
        if asym:
            exl = tgraph.GetErrorXlow(oldpoint) 
            eyl = tgraph.GetErrorYlow(oldpoint) 
            exh = tgraph.GetErrorXhigh(oldpoint) 
            eyh = tgraph.GetErrorYhigh(oldpoint) 
            newtgraph.SetPointError(newpoint, exl, exh, eyl, eyh)
        else:
            ex = tgraph.GetErrorX(oldpoint) 
            ey = tgraph.GetErrorY(oldpoint) 
            newtgraph.SetPointError(newpoint, ex, ey)
    return newtgraph


# code below doesn't work because of TGraph nonsense 
def remove_zero_points_broken_but_should_work_better(tgraph):
    # deal with cpp arrays of doubles as pyroot buffers
    size = tgraph.GetN()
    xbuffer, ybuffer   = tgraph.GetX(),  tgraph.GetY()
    exbuffer, eybuffer = tgraph.GetEXhigh(), tgraph.GetEYhigh()
    
    # make python lists
    xvals  = [ xbuffer[i]  for i in range(size) ]
    exvals = [ exbuffer[i] for i in range(size) ]
    yvals  = [ ybuffer[i]  for i in range(size) ]
    eyvals = [ eybuffer[i] for i in range(size) ]

    # delete the crap
    xvals  = remove_all_zeroes(xvals)
    exvals = remove_all_zeroes(exvals)
    yvals  = remove_all_zeroes(yvals)
    eyvals = remove_all_zeroes(eyvals)
    newsize = len(xvals)
    print(xvals)
    print(exvals)
    print(yvals)
    print(eyvals)

    # numpy array doesn't work for some godunknown reason
    newgraph = TGraphErrors(newsize)
    for i in range(newsize):
        newgraph.SetPoint(i, xvals[i], yvals[i])
        newgraph.SetPointError(i, exvals[i], eyvals[i])
    return newgraph

    # make new graph using numpy.array
    import numpy as np
    xvals  = np.array(xvals)
    exvals = np.array(exvals)
    yvals  = np.array(yvals)
    eyvals = np.array(eyvals)
    return TGraphErrors(size, xvals, yvals, exvals, eyvals)
