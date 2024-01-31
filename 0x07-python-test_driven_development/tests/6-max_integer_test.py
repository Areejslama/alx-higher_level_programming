#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    class to test max value
    """

    def test_max_integer(self):
        """
        function to get max int in a list
        """

        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([3, 4, 6, 7, 9]), 9)
        self.assertEqual(max_integer([6, 8, 9, 12, 4]), 12)
        self.assertEqual(max_integer([-20, -40, -60, -70, -90]), -20)
        self.assertEqual(max_integer([3.2, 4.6, 6.5, 7.4, 9.3]), 9.3)

    def test_wrong_type(self):
        """
        function to test the type
        """

        with self.assertRaises(TypeError):
            max_integer(None)

        with self.assertRaises(TypeError):
            max_integer(["python", 3, 55, -15, "test"])
