"""Numbers for metadata about the luminosity that has been run over for
calculating expected yields etc. The exact numbers may change if the jobs are
re-run.
"""

__author__ = "Sam Cunliffe"
__email__ = "scunliff@cern.ch"

print "WARNING Have just imported kstmm.lumidata last updated 18-06-13"
print "please ensure this is up-to-date otherwise calculations will be out"

import uncertainties as u

# from j.lumi in ganga
DATALUMI2011 = u.ufloat("1016.65608979 +/- 35.5829631426")*1.0e12 # inverse barns
DATALUMI2012 = u.ufloat("2030.83439444 +/- 101.541719722")*1.0e12 # inverse barns
FULLDATALUMI = DATALUMI2011 + DATALUMI2012

# b hadronisation
FU = u.ufloat("40.1 +/- 0.8")*1.0e-2
FD = u.ufloat("40.1 +/- 0.8")*1.0e-2
FS = u.ufloat("10.3 +/- 0.9")*1.0e-2
indrekNumber = u.ufloat("0.35+/-0.05")
FLAMBDA = indrekNumber*(FU+FD)

# from doi:10.1016/j.physletb.2010.10.010 (LHCb paper)
SIGMABBBAR = u.ufloat("284+/-69")*1.0e-6 # barns

