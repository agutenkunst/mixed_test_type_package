import pytest
from mixed_test_type_package.moduleD import ModuleD

def test_moduleD():
    d = ModuleD()
    assert d.return_true()