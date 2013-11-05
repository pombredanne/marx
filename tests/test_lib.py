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

import os

from marx.lib import Lib
from . import resource_root


def test_classes():
    """ Test that classes get properly loaded """

    l = Lib(resource_root)
    classes = list(l.get_classes())
    assert classes == ['class1']

    klass = l.get_class('class1')
    assert klass == {"Hello": "World"}


def test_dockerfiles():
    """ Test that we can list dockerfiles """

    l = Lib(resource_root)
    files = list(l.get_dockerfiles())
    assert files == ["TestImage"]

    assert (os.path.join(
        resource_root,
        'dockerfiles',
        'TestImage'
    ) == l.get_dockerfile('TestImage'))


def test_config():
    """ test that we can load a comfig """

    l = Lib(resource_root)
    obj = l.get_config()
    assert obj == {
        "qwerty": "qwerty"
    }

def test_containers():
    """ test that we can load a container """

    l = Lib(resource_root)
    containers = list(l.get_containers())
    assert ['c1', 'c2'] == containers
