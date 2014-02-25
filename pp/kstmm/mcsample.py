
from utils.stats import counted           # number with sqrt counting error
from utils.paths import MC12STRIPPINGOUT
from kstmm.lumidata import FULLDATALUMI, FD, FS, FLAMBDA, SIGMABBBAR

class MCSample:
    '''Contains all information needed/calculations per MC sample'''
    def __init__(self, codename, title, ngenerator, e_decprodcut, br, colour=1,
                 extracuts="(1 > 0)"):
        self.codename = codename
        self.title = title
        self.ngenerator = counted(ngenerator)
        self.decprodcut = e_decprodcut
        self.br = br
        self.rootcolour = colour
        self.excut = extracuts

    def file_name(self):
        '''Generates the filename to open'''
        return MC12STRIPPINGOUT + "tree_mc2012_" + self.codename + "_newpid_mccor.root" 
  
    def efficiency(self, nsurvive):
        '''Calculate the efficiency to select this background'''
        return counted(nsurvive)/self.ngenerator
  
    def expected_yield(self, nsurvive):
        '''Calculate the expected yield of events in 3/fb'''
  
        # work out which fraction
        if self.codename.count("Bs"):
            hadrF = FS
        elif self.codename.count("Bu") or self.codename.count("Bd"):
            hadrF = FD
        elif self.codename.count("Lb"):
            hadrF = FLAMBDA
        else:
            print "ERROR"
            return real("-1 +/- 0")
    
        nBHadrons = FULLDATALUMI*2*hadrF*SIGMABBBAR
        #print self.codename
        #print hadrF
        #print nBHadrons
        return self.br*nBHadrons*counted(nsurvive)*self.decprodcut/self.ngenerator
  

