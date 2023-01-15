#!/usr/bin/python3
"""Unittest for Base
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Checks for correct output during many edge cases.
    """

    def test_simple(self):
        """Simple tests that the basic program must pass
        """
        Base.reset()
        b1 = Base()
        b2 = Base()
        b3 = Base(33)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 33)
        self.assertEqual(b4.id, 3)

    def test_adv(self):
        """Edge cases that must be accounted for
        """
        Base.reset()
        b5 = Base("string ID")
        b6 = Base((1, 2))
        b7 = Base(None)
        b8 = Base([2, 5])
        self.assertEqual(b5.id, "string ID")
        self.assertEqual(b6.id, (1, 2))
        self.assertEqual(b7.id, 1)
        self.assertEqual(b8.id, [2, 5])


if __name__ == "__main__":
    unittest.main()
