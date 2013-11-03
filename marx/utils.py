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
