#! /usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 17:48:20 2013
@author: gav
Module: jack.py
Description: The interactive commandline client

This is really a learning platform for interactive tools, but as tools develop
they will spun off or incorporated further.

The first tool to be included is the check_winfates_results, with cross-machine
and file movement extensions.

"""
from __future__ import print_function

import sys

from cmd2 import Cmd
### Constants

### Classes
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