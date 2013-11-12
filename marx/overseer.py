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


class Overseer(object):
    def __init__(self, lib):
        self.lib = lib

    def preflight(self):
        checklist = [
            self._init_images,
            self._purge_old_containers,
        ]
        for entry in checklist:
            entry()

    def _init_images(self):
        images = set(
            x['Repository'] for x in self.lib.get_images()
            if 'Repository' in x
        )
        for class_ in self.lib.classes():
            image = class_['image']
            if image not in images:
                print "Building image:", image
                self.lib.build_image(image)

    def _purge_old_containers(self):
        pass
