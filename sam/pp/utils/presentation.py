"""Presentation/housekeeping functions"""
__authors__ = ["Sam Cunliffe"]


def run_webpage_script(path_to_plots):
  """Runs Kostas' web page making script"""
  path_to_script = "/home/hep/stc09/Scripts/createHTMLpageAllPlots.sh"
  command = "%s %s" % (path_to_script, path_to_plots)

  import os
  os.system(command)

  print "finished making webpage"
  return

## idea:  def latexify_plots_like_alex_does
