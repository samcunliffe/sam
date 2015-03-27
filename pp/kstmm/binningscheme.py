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


# one gev bins
b0 = q2bin(0.1, 0.98)
b1 = q2bin(1.1, 2)
b2 = q2bin(2, 3)
b3 = q2bin(3, 4)
b4 = q2bin(4, 5)
b5 = q2bin(5, 6)
b6 = q2bin(6, 7)
b7 = q2bin(7, 8)
b8 = q2bin(11, 11.75)
b9 = q2bin(11.75, 12.5)
b10 = q2bin(15, 16)
b11 = q2bin(16, 17)
b12 = q2bin(17, 18)
b13 = q2bin(18, 19)
b14 = q2bin(1.1, 6.0)
oneGeVbins = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14]

# aaand two GeV biins
a0 = q2bin(0.1, 2)
a1 = q2bin(2, 4)
a2 = q2bin(4, 6)
a3 = q2bin(6, 8)
a4 = q2bin(11, 12.5)
a5 = q2bin(15, 17)
a6 = q2bin(17, 19)
a7 = q2bin(1.1, 6.0)
a8 = q2bin(0.1, 19)
twoGeVbins = [a0, a1, a2, a3, a4, a5, a6, a7] ##, a8]
