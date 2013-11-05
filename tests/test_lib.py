from marx.lib import Lib
from . import resource_root


def test_classes():
    """ Test that classes get properly loaded """

    l = Lib(resource_root)
    classes = list(l.get_classes())
    assert classes == ['class1']

    klass = l.get_class('class1')
    assert klass == {"Hello": "World"}


def test_dockerfiles():
    """ Test that we can list dockerfiles """

    l = Lib(resource_root)
    files = list(l.get_dockerfiles())
    assert files == ["TestImage"]
