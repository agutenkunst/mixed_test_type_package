import pytest
from mixed_test_type_package.moduleE import ModuleE

def test_moduleE():
    e = ModuleE()
    #  Only check this function with pytest, other one with nosetest. 
    #  Please don't do this in production
    assert e.return_true() 