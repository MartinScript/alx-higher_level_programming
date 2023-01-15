#!/usr/bin/python3
"""Unittest for Rectangle
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClass(unittest.TestCase):
    """Checks for correct output during many edge cases.
    """

    def test_simple(self):
        """Simple tests that the basic program must pass
        """
        Base.reset()
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        r3 = Rectangle(5, 6, 0, 0, 44)
        r4 = Rectangle(7, 8)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 44)
        self.assertEqual(r4.id, 3)

    def test_adv(self):
        """Edge cases that must be accounted for
        """
        Base.reset()
        r5 = Rectangle(3, 3, 3, 3, "string ID")
        r6 = Rectangle(3, 3, 3, 3, (1, 2))
        r7 = Rectangle(3, 3, 3, 3, None)
        self.assertEqual(r5.id, "string ID")
        self.assertEqual(r6.id, (1, 2))
        self.assertEqual(r7.id, 1)

    def test_wrong_type(self):
        """Checks for wrong type
        """
        Base.reset()
        with self.assertRaises(TypeError):
            r1 = Rectangle('i', 2)
            r2 = Rectangle(2, 'i')
            r3 = Rectangle(2, 2, 'i')
            r4 = Rectangle(2, 2, 2, 'i')

    def test_wrong_value(self):
        """Checks for wrong value
        """
        Base.reset()
        with self.assertRaises(ValueError):
            r1 = Rectangle(-5, 2)
            r2 = Rectangle(2, -3)
            r3 = Rectangle(2, 2, -3)
            r4 = Rectangle(2, 2, 2, -3)


if __name__ == "__main__":
    unittest.main()
