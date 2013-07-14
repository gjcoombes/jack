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

class Find(Cmd):
    """Find winfates results files"""
    Cmd.prompt = "jack:fetch:find:: "
    machines = []
    project = ""
    LOCDATA_DRIVES = ['e$', 'c$', 'k$']
    RESULT_EXTENSIONS = [".tr3", ".err"]
    locdata_dirs = []
    project_dirs = []
    record = new_fetch_record()

    def _has_locdata(self, machines):
        """Check if the machines have a loc_data directory"""
        result = []
        tpl = r"\\{machine}\{drive}\loc_data"

        for m in machines:
            for d in self.LOCDATA_DRIVES:
                locdata = tpl.format(machine=m, drive=d)
                if osp.isdir(locdata):
                    result.append(locdata)
        return result

    def _has_project(self):
        """Return project dir if the locdata has a project in it"""
        assert self.locdata_dirs
        results = []
        for d in self.locdata_dirs:
            dirs = [ osp.join(d,f, "modelout")
                     for f in fnfilter(os.listdir(d), self.project)
                     if osp.isdir(osp.join(d,f, "modelout")) ]
            results.extend(dirs)
        return results

    def _has_results(self):
        """Return files that match the pattern"""
        assert self.project_dirs
        assert self.patterns
        results = []
        for d in self.project_dirs:
            for p in self.patterns:
                files = [ osp.join(d, f) for f in fnfilter(os.listdir(d), p) ]
                results.extend(files)
        return results

    def _display_locdatas(self):
        """Show the locdatas found on machines"""
        print("Loc_data_dirs found at:")
        for d in self.locdata_dirs:
            print(d)

    def _display_state(self):
        self._display_locdatas()
        self._display

    def _refresh(self):
        """Update state"""
        self._has_locdata()
        self._has_project()

    def do_machines(self, line):
        """Display and set the machines to search within"""
        if line:
            self.machines = line.split()
        if self.machines:
            self.locdata_dirs = self._has_locdata(self.machines)
            self._display_locdatas()
        else:
            print("Perhaps you could try :: machines manta")

    def do_project(self, line):
        """Project can be the whole loc_data name or a pattern

        eg. J0230 - GHD_Apache Phoenix South_1
        or  j0230*
        """
        if line == "":
            jprint(self.project)
        else:
            self.project = line
            self.project_dirs = self._has_project()
            jprint(self.project_dirs)

    def do_patterns(self, line):
        """List of patterns to search modelout results"""
        if line:
            self.patterns = line.split()
        else:
            jprint(self.patterns)
        if self.patterns:
            self.files = self._has_results()
            for f in self.files:
                print(f)

### Functions

if __name__ == "__main__":

    app = Jack()
    app.cmdloop()









    print("Done __main__")