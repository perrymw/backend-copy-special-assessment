#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse
import sys

# This is to help coaches and graders identify student assignments
__author__ = "perrymw ---help from Alec Stephens"


# +++your code here+++
"""get_special_paths(dir) -- returns a list of the absolute paths of the special files in the given directory"""
def get_special_paths(dirr):
    stack = []
    path_o_direct = os.listdir(dirr)
    for files in path_o_direct:
        reggie_search = re.search(r'__(\w+)__', files)
        if reggie_search:
            stack.append(os.path.abspath(os.path.join(dirr, files)))
    return(stack)

"""copy_to(paths, dir) given a list of paths, copies those files into the given directory"""
def copy_to(paths, dir):
    if not os.path.exists(dir):
        os.mkdir(dir)
    for p in paths:
        file_name = os.path.basename(p)
        shutil.copy(p, os.path.join(dir, file_name))
    


"""zip_to(paths, zippath) given a list of paths, zip those files up into the given zipfile"""
"""if file doesn't exist, print error"""
def zip_to(paths, zippath):
    cmd = ["zip", "-j", zippath]
    print("Command I'm going to do: ")
    print ('{} {} {}'.format(cmd[0], cmd[1], cmd[2]))
    try:
        cmd.extend(paths)
        subprocess.check_output(cmd)
    except IOError:
        print("zip I/O error: No such file or directory")
    
def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='the directory to read files from')
    return parser

def main():
    # This snippet will help you get started with the argparse module.
    parser = create_parser()
    # TODO need an argument to pick up 'from_dir'
    args = parser.parse_args()

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.
    
    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).
    if not args:
        parser.print_usage()
        sys.exit(1)

    # +++your code here+++
    # Call your functions
    path_names = []
    for dirr in args.from_dir:
        path_names.extend(get_special_paths(dirr))
    if args.todir:
        copy_to(path_names, args.todir)
    elif args.tozip:
        zip_to(path_names, args.tozip)
    else:
        print ('/n'.join(path_names))
        


if __name__ == "__main__":
    main()
