# Command line history:
import readline

HISTFILE = os.path.expanduser("~/.pdbhist")
try:
    readline.read_history_file(HISTFILE)
except IOError:
    pass

import atexit
atexit.register(readline.write_history_file, HISTFILE)
readline.set_history_length(1000)

# cleanup
del HISTFILE
del readline
del atexit
