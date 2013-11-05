from marx.lib import Lib
from . import resource_root


def test_classes():
    l = Lib(resource_root)
    print l.get_classes()
