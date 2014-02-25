from ROOT import TTree
import ROOT as r
from array import array

def __AddVar__(self, var, name, res, use_double=True):
    """Add variable branch to the tree"""
    has_branche = res.has_key(name)
            
    if has_branche:
        res[name][0] = float(var)
    else :
        if use_double :
            print "branch ", name, " as Double "
            comp = array('d', [0])
            self.Branch(name, comp, name+'/D')
            comp[0]= r.Double(var)
            aux = {name: comp}
            res.update(aux)
        else :
            print "branch ", name, " as Float "
            comp = array('f', [0])
            self.Branch(name, comp, name+'/F')
            comp[0]= float(var)
            aux = {name: comp}
            res.update(aux)
    return res

TTree.AddVar = __AddVar__ # dynamically add to TTree class



def __FillVars__(self, res_tuple):
    """fill the branches in the dictionary"""
    for name, val in res_tuple.iteritems() : 
        b = self.GetBranch(name) 
        b.Fill()

TTree.FillVars = __FillVars__




def __AddVarInt__(self, var, name, res):
    """Add integer variable to the tree"""
    has_branche = res.has_key(name)

    if has_branche:
        res[name][0] = int(var)
    else:
        comp = array('i', [0])
        self.Branch(name, comp, name+'/I')
        comp[0]= int(var)
        aux = {name: comp}
        res.update(aux)
    return res
        
TTree.AddVarInt = __AddVarInt__

