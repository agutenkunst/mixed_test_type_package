import unittest
from mixed_test_type_package.moduleE import ModuleE

class TestModuleE(unittest.TestCase):
    def test(self):
        e = ModuleE()
        self.assertFalse(e.return_false())
        return

if __name__ == '__main__':
    unittest.main()
