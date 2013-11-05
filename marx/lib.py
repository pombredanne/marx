# -*- coding: utf-8 -*-
# Marx, the worker overseer based on docker.
# Copyright © 2013, Paul R. Tagliamonte <tag@pault.ag>
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.

import glob
import json
import os


class Lib(object):
    """
    Object that allows access to the marx lib directory, for dynamic
    (and persistant) data.
    """

    def __init__(self, directory):
        """
        `directory' is a path (absolute) to the marx lib.
        """
        self.directory = directory

    def _json_listing(self, path):
        """
        List json files in path `path'
        """
        flag = ".json"
        for entry in glob.iglob(os.path.join(path, "*%s" % (flag))):
            entry = os.path.basename(entry)
            if entry.endswith(flag):
                entry = entry[:-len(flag)]
            yield entry

    def _file_listing(self, path):
        """
        Return a file listing for path `path'
        """
        return os.listdir(path)

    def _load_json(self, path):
        """
        Returned a parsed json file.
        """
        return json.load(open(path, 'r'))

    def get_classes(self):
        """
        Get all the classdefs by name
        """
        return self._json_listing(os.path.join(self.directory, 'classes'))

    def get_class(self, what):
        """
        Load a classdef
        """
        return self._load_json(os.path.join(
            self.directory,
            'classes', "%s.json" % (what))
        )

    def get_containers(self):
        """
        Get our containers
        """
        return self._json_listing(os.path.join(self.directory, 'containers'))

    def get_dockerfiles(self):
        """
        Get dockerfiles
        """
        return self._file_listing(os.path.join(self.directory, 'dockerfiles'))

    def get_dockerfile(self, fp):
        """
        Get dockerfiles
        """
        return os.path.join(self.directory, 'dockerfiles', fp)

    def get_config(self):
        """
        """
        return self._load_json(os.path.join(
            self.directory,
            "config.json"
        ))
