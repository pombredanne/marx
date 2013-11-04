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

import re

from .parser import parse_list_output
from ..utils import run_command, run_long_command


class Docker(object):
    def __init__(self, binary='docker'):
        self._binary = binary

    def _cmd(self, command, *args, **kwargs):
        cmd = [self._binary,] + [command, ] + [
            "-%s=%s" % (x, kwargs[x]) for x in kwargs
        ] + list(args)
        return cmd

    def _invoke(self, *args, **kwargs):
        cmd = self._cmd(*args, **kwargs)
        out, err, ret = run_command(cmd)
        return out, err, ret

    def _long_invoke(self, *args, **kwargs):
        cmd = self._cmd(*args, **kwargs)
        return run_long_command(cmd)

    def images(self, **kwargs):
        out, err, ret = self._invoke("images", **kwargs)
        return parse_list_output(out)

    def ps(self, **kwargs):
        out, err, ret = self._invoke("ps", **kwargs)
        return parse_list_output(out)

    def top(self, container, **kwargs):
        out, err, ret = self._invoke("top", container, **kwargs)
        return parse_list_output(out)

    def history(self, image, **kwargs):
        out, err, ret = self._invoke("history", image, **kwargs)
        return parse_list_output(out)

    def attach(self, container, **kwargs):
        return self._long_invoke("attach", container, **kwargs)

    def rm(self, *args, **kwargs):
        args = list(args)
        if args == []:
            raise ValueError("Need at least one container")
        out, err, ret = self._invoke("rm", *args, **kwargs)
        return self._rm_out(out)

    def rmi(self, *args, **kwargs):
        args = list(args)
        if args == []:
            raise ValueError("Need at least one container")
        out, err, ret = self._invoke("rmi", *args, **kwargs)
        return self._rm_out(out)

    def _rm_out(self, out):
        for line in out.splitlines():
            if line.startswith("Error:"):
                continue
            if line.strip() == "":
                continue
            yield line

    def events(self, **kwargs):
        for event in self._long_invoke("events", **kwargs):
            yield re.match(
                (".*\[(?P<when>.*)\] (?P<container>.*): "
                 "\(from (?P<image>.*):(?P<tag>.*)\) (?P<action>.*).*"),
                event).groupdict()

    def run(self, image, command, *args, **kwargs):
        if "d" in kwargs:  # Detached
            out, err, ret = self._invoke("run", image, command, *args, **kwargs)
            return out.strip()
        else:
            return self._long_invoke("run", image, command, *args, **kwargs)
