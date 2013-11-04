# Marx, the worker overseer based on docker.
# Copyright (C) 2013, Paul R. Tagliamonte <tag@pault.ag>
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

def parse_list_output(stream):
    stream = iter(stream.splitlines())
    header_ = next(stream)
    header = header_.split()
    info = [(x, header_.index(x)) for x in header]
    i1 = iter(info + [(None, None)])
    i2 = iter(info)
    next(i1)  # To offset the lists.
    split = zip(i2, i1)

    for entry in stream:
        entries = {}
        for fro, to in split:
            name, start = fro
            name = name.lower()
            _, end = to
            if end is None:
                entries[name] = entry[start:]
            else:
                entries[name] = entry[start:end]
            entries[name] = entries[name].strip()
        yield entries
