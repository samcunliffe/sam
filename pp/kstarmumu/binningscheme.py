
from sam.pp.q2bin import q2bin

bin0 = q2bin(0.1, 2)
bin1 = q2bin(2, 4.3)
bin2 = q2bin(4.3, 10.09)
bin3 = q2bin(10.09, 14.18)
bin4 = q2bin(14.18, 16)
bin5 = q2bin(16, 19)

q2bins = [bin0, bin1, bin2, bin3, bin4, bin5]

print bin2
print bin2.simple_title
print bin2.latex_title
print bin2.cut
