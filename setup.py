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

from marx import __appname__, __version__
from setuptools import setup


long_description = ""

setup(
    name=__appname__,
    version=__version__,
    scripts=[],
    packages=[
        'marx',
        'marx.docker',
    ],
    author="Paul Tagliamonte",
    author_email="tag@pault.ag",
    long_description=long_description,
    description='Control the means of production',
    license="GPL-2+",
    url="http://deb.io/",
    platforms=['any'],
    entry_points={
        'console_scripts': [
        ],
    }
)
