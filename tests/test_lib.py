from marx.lib import Lib
from . import resource_root


def test_classes():
    l = Lib(resource_root)
    classes = list(l.get_classes())
    assert classes == ['class1']

    klass = l.get_class('class1')
    assert klass == {"Hello": "World"}
