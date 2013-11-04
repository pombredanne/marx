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
import time
import fcntl
import shlex
import subprocess
from cStringIO import StringIO


def run_command(command, stdin=None):
    if not isinstance(command, list):
        command = shlex.split(command)
    try:
        pipe = subprocess.Popen(command, shell=False,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
    except OSError:
        return (None, None, -1)

    kwargs = {}
    if stdin:
        kwargs['input'] = stdin.read()

    (output, stderr) = pipe.communicate(**kwargs)
    output, stderr = (c.decode('utf-8',
                               errors='ignore') for c in (output, stderr))
    return (output, stderr, pipe.returncode)


def run_long_command(command, stdin=None):
    if not isinstance(command, list):
        command = shlex.split(command)

    pipe = subprocess.Popen(command, shell=False,
                            #stdin=subprocess.PIPE,
                            stdin=None,
                            stdout=subprocess.PIPE,
                            #stderr=subprocess.PIPE)
                            stderr=None)

    def iterpipe(pipe):
        fl = fcntl.fcntl(pipe.stdout, fcntl.F_GETFL)
        fcntl.fcntl(pipe.stdout, fcntl.F_SETFL, fl | os.O_NONBLOCK)

        while True:
            pipe.poll()
            if pipe.returncode is not None:
                for line in pipe.stdout.readlines():
                    yield line
                return
            try:
                x = pipe.stdout.readline().strip()
            except IOError:
                time.sleep(0.1)
                continue

            yield x.decode('utf-8', errors='ignore')

    return iterpipe(pipe)
