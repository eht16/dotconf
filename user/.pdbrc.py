# Command line history:
import os
import readline

HISTFILE = os.path.expanduser("~/.pdbhist")
try:
    readline.read_history_file(HISTFILE)
except IOError:
    pass

import atexit
atexit.register(readline.write_history_file, HISTFILE)
readline.set_history_length(1000)
del HISTFILE

# Cleanup any variables that could otherwise clutter up the namespace.
try:
    del atexit
    del os
    del readline
    del rlcompleter
except NameError:
    # Probably this is a second pdbrc that has been loaded.
    pass
