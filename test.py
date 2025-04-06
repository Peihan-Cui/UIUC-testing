import unittest

class MyTests(unittest.TestCase):
    def test_add(self):
        assert 1 + 1 == 2
        self.assertEqual(2 + 2, 4)

    def helper(self):
        assert False

def test_direct():
    assert True
