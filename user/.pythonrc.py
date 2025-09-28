#!/usr/bin/env python

# Inspired by https://github.com/dcramer/dotfiles/blob/master/python/pythonrc.py

import atexit
import os
import readline
import rlcompleter

readline.parse_and_bind('tab: complete')
readline.set_history_length(1024 * 10)
history = os.path.expanduser("~/.pythonhist")

def save_history(history=history):
    import readline
    readline.write_history_file(history)

if os.path.exists(history):
    try:
        readline.read_history_file(history)
    except IOError:
        pass


# initialize Django if available
try:
    from django.core.management import setup_environ
    import settings
    setup_environ(settings)
    del settings, setup_environ
except:
    pass

atexit.register(save_history)
del os, atexit, readline, rlcompleter, save_history, history
