"""Some things for consistent plots and regions of bmass"""

BMASSHISTOBINNINGSCHEME = (100, 5180, 5780)

SIGWINLOW =  5230.0
SIGWINHIGH = 5330.0

SIGWIN = "B0_MM > %f && B0_MM < %f" % (SIGWINLOW, SIGWINHIGH)
