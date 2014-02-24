
#from sam.pp.kinematics.two_body_phsp import two_body_phsp_q
from two_body_phsp import two_body_phsp_q
import matplotlib.pyplot as p

mkpi = range(600, 1200)
q = [two_body_phsp_q(5280, 3090, x) for x in mkpi]

p.plot(mkpi, q)
p.savefig("test_plot_b2kstmm.png")

q = [two_body_phsp_q(x, 493.67, 139.57) for x in mkpi]
p.plot(mkpi, q)
p.savefig("test_plot_kst2kpi.png")
