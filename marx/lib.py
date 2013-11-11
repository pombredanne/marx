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

from .core import client

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
        self._ensure_exists(self.directory)
        self._ensure_exists(os.path.join(self.directory, 'classes'))
        self._ensure_exists(os.path.join(self.directory, 'containers'))
        self._ensure_exists(os.path.join(self.directory, 'dockerfiles'))

    def _ensure_exists(self, path):
        if not os.path.exists(path):
            os.mkdir(path)

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

    def _write_json(self, name, class_, obj):
        path = os.path.join(self.directory, class_, "%s.json" % (name))
        # Schema validate.
        json.dump(obj, open(path, 'w'))

    def _remove_json(self, name, class_):
        path = os.path.join(self.directory, class_, "%s.json" % (name))
        # Schema validate.
        os.unlink(path)

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

    def add_container(self, name, obj):
        return self._write_json(name, 'containers', obj)

    def remove_container(self, name):
        return self._remove_json(name, 'containers')

    def get_container(self, name):
        return self._load_json(os.path.join(
            self.directory,
            'containers',
            "%s.json" % (name)
        ))

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

    def get_images(self):
        return client.images()

    def get_image(self, image):
        return client.images(name=image)

    def build_image(self, name, rebuild=False):
        info = self.get_image(name)
        if info and rebuild is False:
            raise Exception("Image already exists, bronie")

        image = open(self.get_dockerfile(name), 'r')
        client.build(
            tag=name,
            quiet=False,
            fileobj=image,
            # nocache=False,
            nocache=True,
            rm=True,
        )


def default_lib():
    return Lib(os.path.expanduser("~/.marx"))
