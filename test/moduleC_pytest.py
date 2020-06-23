import pytest
from mixed_test_type_package.moduleC import ModuleC

def test_moduleC():
    c = ModuleC()
    assert c.return_true()