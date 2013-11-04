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

from marx.docker.wrapper import Docker

d = Docker()

#for x in d.rm(*[x['id'] for x in d.ps(a=True)]):
#    print "Removed: %s" % (x)

hsh = d.run("ubuntu", "echo", "hello", d=True)
