#!/usr/bin/python3
"""Unittest for Square
"""
import unittest
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle


class TestSquareClass(unittest.TestCase):
    """Checks for correct output during many edge cases.
    """

    def test_simple(self):
        """Simple tests that the basic program must pass
        """
        Base.reset()
        s1 = Square(1)
        s2 = Square(3)
        s3 = Square(5, 6, 7, 44)
        s4 = Square(8, 9, 9)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s3.id, 44)
        self.assertEqual(s4.id, 3)

    def test_adv(self):
        """Edge cases that must be accounted for
        """
        Base.reset()
        s5 = Square(3, 3, 3, "string ID")
        s6 = Square(3, 3, 3, (1, 2))
        s7 = Square(3, 3, 3, None)
        self.assertEqual(s5.id, "string ID")
        self.assertEqual(s6.id, (1, 2))
        self.assertEqual(s7.id, 1)

    def test_wrong_type(self):
        """Checks for wrong type
        """
        Base.reset()
        with self.assertRaises(TypeError):
            s1 = Square('i', 2)
            s2 = Square(2, 'i')
            s3 = Square(2, 2, 'i')

    def test_wrong_value(self):
        """Checks for wrong value
        """
        Base.reset()
        with self.assertRaises(ValueError):
            s1 = Square(-5, 2)
            s2 = Square(2, -3)
            s3 = Square(2, 2, -3)


if __name__ == "__main__":
    unittest.main()
