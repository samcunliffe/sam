
"""Takes a rootfile input and makes a directory of pdf versions of the plots"""

from sam.pp.utils.root import get_plots

def parse_options():
    """parse all options for this script"""
    from optparse import OptionParser
    op = OptionParser()
    op.add_option("--file", dest="filename", help="a file of plots")
    op.add_option("--pdf", dest="pdf", action="store_true", help="make pdfs")
    op.add_option("--png", dest="png", action="store_true", help="make pngs")
    (options, args) = op.parse_args()
    if not options.filename:
        op.print_help()
        exit()
    return options


def mkdir(dirname):
    """makes a directory"""
    from os import system as run_command
    return run_command("mkdir -p " + dirname)


def save_plot(plot, dirname, pdf, png):
    """makes pdf and/or png plots"""
    from sam.pp.utils.root import save_plot as internal_save_function
    stem = dirname + '/' + plot.GetName()
    if pdf: internal_save_function(plot, stem + '.pdf', '', None, False)
    if png: internal_save_function(plot, stem + '.png', '', None, False)
    return



if __name__ == "__main__":
    opts = parse_options()
    print "Will run over:", opts.filename
    dirname = opts.filename.replace(".root", "") 
    mkdir(dirname)
    fi, plots = get_plots(opts.filename)
    print plots
    [save_plot(p, dirname, opts.pdf, opts.png) for p in plots]
    fi.Close()
