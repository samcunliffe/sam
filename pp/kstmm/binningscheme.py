"""Usage:

# safe way, keeping namespace
import kstmm
print kstmm.binningscheme.q2bins

# less typing, less secure (be careful of scope)
from kstmm.binningscheme import *
print q2bins

"""

from kstmm.q2bin import q2bin

bin0 = q2bin(0.1, 2)
bin1 = q2bin(2, 4.3)
bin2 = q2bin(4.3, 10.09)
bin3 = q2bin(10.09, 14.18)
bin4 = q2bin(14.18, 16)
bin5 = q2bin(16, 19)
bin6 = q2bin(1, 6)
bin7 = q2bin(6, 19)
q2bins = [bin0, bin1, bin2, bin3, bin4, bin5, bin6, bin7]
