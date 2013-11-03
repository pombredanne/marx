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
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    def iterpipe(pipe):
        while True:
            x = pipe.stdout.readline().strip()
            pipe.poll()
            if pipe.returncode is not None:
                return
            yield x
    return iterpipe(pipe)
