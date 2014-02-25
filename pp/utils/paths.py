"""Paths to data"""

# TODO add something here to look at the hostname and adjust paths accordingly

SAMVOLS = "/vols/lhcbdisk04/scunliffe/Kstmm/"
DATAPRESELECTED = SAMVOLS + "Data/Preselected/"
DATASELECTED = SAMVOLS + "Data/Selected/"
MC12STRIPPINGOUT = SAMVOLS + "MC12/StrippingOut/"

SAMWEB = "/home/hep/stc09/public_html/B0-KstarMuMu/Swave/"

import os
def mkdir(s):   os.system("mkdir " + s)
def mkdir_p(s): os.system("mkdir -p " + s)
