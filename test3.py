import unittest

class BaseTestCase(unittest.TestCase):
    def test_base_assertion(self):
        assert 1 == 1

    def test_self_assertion(self):
        self.assertTrue(True)

    def helper_function(self):
        assert "hello" == "hello"


class InheritedTestCase(BaseTestCase):
    def test_custom(self):
        self.helper_function()
