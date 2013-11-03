from .parser import parse_list_output
from ..utils import run_command


class Docker(object):
    def __init__(self, binary='docker'):
        self._binary = binary

    def _invoke(self, *args):
        out, err, ret = run_command([
            self._binary,
        ] + list(args))
        return out, err, ret

    def images(self):
        out, err, ret = self._invoke("images")
        return parse_list_output(out)
