from .parser import parse_list_output
from ..utils import run_command


class Docker(object):
    def __init__(self, binary='docker'):
        self._binary = binary

    def _invoke(self, *args, **kwargs):
        cmd = [self._binary, ] + list(args) + [
            "-%s=%s" % (x, kwargs[x]) for x in kwargs]
        out, err, ret = run_command(cmd)
        return out, err, ret

    def images(self, **kwargs):
        out, err, ret = self._invoke("images", **kwargs)
        return parse_list_output(out)

    def ps(self, **kwargs):
        out, err, ret = self._invoke("ps", **kwargs)
        return parse_list_output(out)
