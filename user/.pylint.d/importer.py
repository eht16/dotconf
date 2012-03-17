#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os


#----------------------------------------------------------------------
def add_eggs(path):
    egg_base_path = os.path.join(path, 'eggs')
    if not os.path.exists(egg_base_path):
        return
    for egg in os.listdir(egg_base_path):
        egg_path = os.path.join(egg_base_path, egg)
        if os.path.exists(egg_path):
            sys.path.insert(1, egg_path)


#----------------------------------------------------------------------
def fix_paths():
    cwd = os.getcwd()
    cwd_parts = cwd.split('/')
    idx = len(cwd_parts) - 1

    if cwd_parts[-1] == 'bin':
        include_path = '/'.join(cwd_parts[:-1]) + '/include'
        if os.path.exists(include_path):
            sys.path.insert(0, include_path)
            add_eggs('/'.join(cwd_parts[:-1]))
    elif os.path.exists(os.path.join(cwd, 'include')):
        include_path = os.path.join(cwd, 'include')
        if os.path.exists(include_path):
            sys.path.insert(0, include_path)
            add_eggs(cwd)
    else:
        while idx >= 0 and cwd_parts[idx] != 'include' and cwd_parts[idx] != '/':
            idx -= 1
            # if we find a license file, assume this is the top-level directory
            if os.path.exists(os.path.join('/'.join(cwd_parts[:idx + 1]), 'COPYING')):
                break

        include_path_parts = cwd_parts[:idx + 1]
        if include_path_parts:
            include_path = '/'.join(include_path_parts)
            if os.path.exists(include_path):
                sys.path.insert(0, include_path)
                add_eggs('/'.join(include_path_parts[:-1]))


fix_paths()
