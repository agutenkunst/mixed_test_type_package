import unittest
from mixed_test_type_package.moduleB import ModuleB

class TestModuleB(unittest.TestCase):
    def test(self):
        b = ModuleB()
        self.assertTrue(b.return_true())
        return

if __name__ == '__main__':
    unittest.main()
