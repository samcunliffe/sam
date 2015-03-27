
from kstmm.vars import Variable # the base class

class PidVariable(Variable):
    """Specific case of the 'variable' which is pid and has two branch names"""

    def __init__(self, name, title, binningscheme, dllform):

        # instantiate the baseclass explicitly
        # (with no units)
        Variable.__init__(self, name, title, binningscheme, "", dllform)
        self.dllform = self.branchname

        # find the 'PID' version of this variable
        if dllform.count("BDT"):
            self.pidform = dllform.replace("_DLL", "") # my convention for bdts
        else:
            self.pidform = dllform.replace("DLL", "PID")
        return


pid_variables = [

    # dlls
    PidVariable("K_idK", "K DLL_{K-#pi}", (50, -50, 200), "K_DLLK"),
    PidVariable("pi_idK", "#pi DLL_{K-#pi}", (50, -200, 50), "Pi_DLLK"),
    PidVariable("pi_idp", "#pi DLL_{p-#pi}", (50, -200, 50), "Pi_DLLp"),
    PidVariable("mup_idmu", "#mu^{+} DLL_{#mu-#pi}", (50, -10, 20), "Muplus_DLLmu"),
    PidVariable("mum_idmu", "#mu^{-} DLL_{#mu-#pi}", (50, -10, 20), "Muminus_DLLmu"),
    PidVariable("diag", "K DLL_{K-#pi} - #pi DLL_{K-#pi}", (50, -5, 250), "(K_DLLK - Pi_DLLK)"),

    # kinematics/ detector
    PidVariable("nTracks", "track occupancy",  (50, 0, 600), "nTracks"),
    PidVariable("K_PT", "p_{T}(K) (MeV/c)",    (50, 0, 20000), "K_PT"),
    PidVariable("Pi_PT", "p_{T}(#pi) (MeV/c)", (50, 0, 20000), "Pi_PT"),
    PidVariable("K_P", "p(K) (MeV/c)",       (50, 0, 50000), "K_P"),
    PidVariable("Pi_P", "p(#pi) (MeV/c)",    (50, 0, 500000), "Pi_P"),
    PidVariable("B0_P", "p(B) (MeV/c)",      (50, 0, 500000), "B0_P"),
    PidVariable("B0_PT", "p_{T}(B) (MeV/c)",   (50, 0, 60000), "B0_PT"),
    PidVariable("B0_eta", "#eta(B)",           (50, 1.9, 6.1), "B0_ETA"),
    PidVariable("vertex", "vertex quality", (40, 0, 8), "VertexChi2OverNdof"),

    # maricn iso
    PidVariable("MarcinMup", "Muon isolation", (30, 0, 15), "Muplus_isolation_V2_15"),
    PidVariable("MarcinMum", "Muon isolation", (30, 0, 15), "Muminus_isolation_V2_15"),

    # lphne iso
    PidVariable("kaon_isolation", "LPHNE kaon isolation", (12, 0, 6), "kaon_isolation"),
    PidVariable("pion_isolation", "LPHNE pion isolation", (12, 0, 6), "pion_isolation"),

    # bdts
    PidVariable("bdt01", "BDT 01 response", (50, -1.1, 1.1), "BDT_FreezeDec13_DLL_1"),
    PidVariable("bdt02", "BDT 02 response", (50, -1.1, 1.1), "BDT_FreezeDec13_DLL_2"),
    PidVariable("bdt03", "BDT 03 response", (50, -1.1, 1.1), "BDT_FreezeDec13_DLL_3"),
    PidVariable("bdt04", "BDT 04 response", (50, -1.1, 1.1), "BDT_FreezeDec13_DLL_4"),
    PidVariable("bdt05", "BDT 05 response", (50, -1.1, 1.1), "BDT_FreezeDec13_DLL_5"),
    PidVariable("bdt06", "BDT 06 response", (50, -1.1, 1.1), "BDT_FreezeDec13_DLL_6"),
    PidVariable("bdt07", "BDT 07 response", (50, -1.1, 1.1), "BDT_FreezeDec13_DLL_7"),
    PidVariable("bdt08", "BDT 08 response", (50, -1.1, 1.1), "BDT_FreezeDec13_DLL_8"),
    PidVariable("bdt09", "BDT 09 response", (50, -1.1, 1.1), "BDT_FreezeDec13_DLL_9"),
    PidVariable("bdt10", "BDT 10 response", (50, -1.1, 1.1), "BDT_FreezeDec13_DLL_10"),
    PidVariable("bdt",   "BDT", (50, 0.0, 1.1), "BDT"),
    #PidVariable("bdt", "placeholder BDT response", (50, -1.1, 1.1), "BDT10May13A_DLL"),
]
