#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os


def fix_paths():
    cwd = os.getcwd()
    cwd_parts = cwd.split('/')
    idx = len(cwd_parts) - 1
    if cwd_parts[-1] == 'bin':
        include_path = '/'.join(cwd_parts[:-1]) + '/include'
        if os.path.exists(include_path):
            sys.path.insert(0, include_path)
    elif os.path.exists(os.path.join(cwd, 'include')):
        include_path = os.path.join(cwd, 'include')
        if os.path.exists(include_path):
            sys.path.insert(0, include_path)
    else:
        while idx >= 0 and cwd_parts[idx] != 'include' and cwd_parts[idx] != '/':
            idx -= 1

        include_path_parts = cwd_parts[:idx+1]
        if include_path_parts:
            include_path = '/'.join(include_path_parts)
            if os.path.exists(include_path):
                sys.path.insert(0, include_path)


fix_paths()
