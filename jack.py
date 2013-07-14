#! /usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 17:48:20 2013
@author: gav
Module: jack.py
Description: The interactive commandline client

This is really a learning platform for interactive tools, but as tools develop
they will spun off, or incorporated further.

The first tool to be included is the check_winfates_results, with cross-machine
search and file movement extensions.

"""
from __future__ import print_function

import sys
import os
import os.path as osp
from pprint import pprint
from fnmatch import filter as fnfilter

from cmd2 import Cmd
### Constants

### Classes

def new_fetch_record():
    """Return a default fetch record (dict) for filling in

    type: fetch - from Jack perhaps
    header: Contains everything needed to generate the body
        paths: List of directories to search
        patterns: List of patterns to apply
        match_type: glob or regex
        clobber: Overwrite files? default: True
        cleanup: Delete fiels after they are moved? default - False for the moment
    body: The payload to be executed or fetched
        dest_dir: The directory to move files to
        files:
    """
    return {"type": "fetch",
            "header": {
                "paths": [],
                "patterns": [],
                "match_type": "glob",
                "clobber": True,
                "cleanup": False,
                },
            "body": {
                "files": [],
                },
            }

class Jack(Cmd):
    """Commandline interpreter to access various tools

    """
    Cmd.prompt = "Jack says:"

    def do_speak(self, *args):
        """Tell me what you do"""
        msg = "This is what I can do.\n"
        sys.stdout.write(msg)
### Functions

if __name__ == "__main__":

    app = Jack()
    app.cmdloop()









    print("Done __main__")