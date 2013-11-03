import re

from .parser import parse_list_output
from ..utils import run_command, run_long_command


class Docker(object):
    def __init__(self, binary='docker'):
        self._binary = binary

    def _cmd(self, *args, **kwargs):
        cmd = [self._binary, ] + list(args) + [
            "-%s=%s" % (x, kwargs[x]) for x in kwargs]
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

    def events(self, **kwargs):
        for event in self._long_invoke("events", **kwargs):
            yield re.match(
                (".*\[(?P<when>.*)\] (?P<container>.*): "
                 "\(from (?P<image>.*):(?P<tag>.*)\) (?P<action>.*).*"),
                event).groupdict()
