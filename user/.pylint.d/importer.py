#!/usr/bin/env python
# -*- coding: utf-8 -*-


import glob
import os
import sys


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
def detect_and_add_virtualenv_for_django(path):
    # look for virtualenv
    env_path = os.path.join(path, 'env')
    if not os.path.exists(env_path):
        env_path = os.path.join(path, 'venv')
        if not os.path.exists(env_path):
            # give up
            return
    # use glob to find the path with some Python
    site_packages_path = u'%s/lib/python?.?/site-packages' % env_path
    site_packages = glob.glob(site_packages_path)
    if len(site_packages) == 1:
        sys.path.extend(site_packages)


#----------------------------------------------------------------------
def fix_paths():
    cwd = os.getcwd()
    cwd_parts = cwd.split('/')
    idx = len(cwd_parts) - 1

    if cwd_parts[-1] == 'bin':
        # in the bin/ directory
        include_path = '/'.join(cwd_parts[:-1]) + '/include'
        if os.path.exists(include_path):
            sys.path.insert(0, include_path)
            add_eggs('/'.join(cwd_parts[:-1]))
    elif os.path.exists(os.path.join(cwd, 'include')):
        # on top-level project directory
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
            # if we find a manage.py, this is most certainly the top of a Django (1.4) project
            if os.path.exists(os.path.join('/'.join(cwd_parts[:idx + 1]), 'manage.py')):
                break
            # if we find a license file, assume this is the top-level directory
            if os.path.exists(os.path.join('/'.join(cwd_parts[:idx + 1]), 'LICENSE')):
                break
            # if we find a requirements.txt, this is may be the top of a project
            if os.path.exists(os.path.join('/'.join(cwd_parts[:idx + 1]), 'requirements.txt')):
                break
            # if we find a MANIFEST.in, this is may be the top of a project
            if os.path.exists(os.path.join('/'.join(cwd_parts[:idx + 1]), 'MANIFEST.in')):
                break

        include_path_parts = cwd_parts[:idx + 1]
        if include_path_parts:
            include_path = '/'.join(include_path_parts)
            if os.path.exists(include_path):
                sys.path.insert(0, include_path)
                add_eggs('/'.join(include_path_parts[:-1]))
            detect_and_add_virtualenv_for_django(include_path)


fix_paths()
