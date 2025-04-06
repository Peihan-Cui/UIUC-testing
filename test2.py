import unittest

def helper_assertion():
    assert 1 + 1 == 2

def another_helper():
    helper_assertion()

class MyTests(unittest.TestCase):

    def test_raw_assert(self):
        assert True

    def test_self_assert(self):
        self.assertEqual(2, 1 + 1)

    def test_indirect_call(self):
        helper_assertion()

    def test_nested_call(self):
        another_helper()

def test_standalone():
    assert "hello".upper() == "HELLO"
