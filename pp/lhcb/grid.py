
import uncertainties as u
def job_selection_efficiency(DecProdEff,DecProdEffErr,nSelected,nRunOver):
  from math import sqrt as s
  e_dpc = u.ufloat((DecProdEff,DecProdEffErr))
  nsel  = u.ufloat((nSelected,s(nSelected)))
  nrun  = u.ufloat((nRunOver,s(nRunOver)))
  out   = e_dpc*nsel/nrun
  print "(", 100*out, ") %"
  return out
