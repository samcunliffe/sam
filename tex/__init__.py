"""Stuff for making LaTeX tables, since pytable is broken at the moment"""

from sam.utils import is_string

def list_to_textable_row(li):
    out = ''
    for entry in li: 
        if is_string(entry): out += entry + ' & '
        else:                out += '%.2f & ' % entry
    out = out[:-2]
    out += r'\\'
    return out

def array_to_textable(list_of_lists, filename):
    """takes an array (a list of lists) and formats it into a latex table"""
    if not filename.endswith('.tex'): filename += '.tex'
    table = open(filename, "w")
    table.write(r"\begin{table}" + "\n")
    table.write(r"\begin{tabular}{" + " c"*len(list_of_lists[0]) + " }" + "\n")
    for row in list_of_lists[:-1]:
        table.write( list_to_textable_row(row) + "\n" )
    table.write( list_to_textable_row(row)[:-2] + "\n" ) # trim the last '\\'
    table.write(r"\end{tabular}" + "\n")
    table.write(r"\end{table}" + "\n")
    table.close()
    print 'made a tex table: %s' % filename
    return
