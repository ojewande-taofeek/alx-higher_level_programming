#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """The class for the max_integer unit testing"""
    def test_values(self):
        """Test if the arg is an instance of list"""
        my_list = [1, 2, 5, 3, 4]
        self.assertEqual(5, max_integer(my_list))
        my_list = [5, 2, 1, 3, 4]
        self.assertEqual(5, max_integer(my_list))
        my_list = [1, 2, 4, 3, 5]
        self.assertEqual(5, max_integer(my_list))
        my_list = [1, 2, 5, -3, 4]
        self.assertEqual(5, max_integer(my_list))
        my_list = [-1, -2, -5, -3, -4]
        self.assertEqual(-1, max_integer(my_list))
        my_list = [-1]
        self.assertEqual(-1, max_integer(my_list))
        self.assertEqual(None, max_integer())

    def test_instance(self):
        """Test if the arg is an instance of list"""
        my_list = [1, 2, 5, 3, 4]
        self.assertIsInstance(my_list, list)
        new_list = "try"
        self.assertNotIsInstance(new_list, list)

    def test_not_an_int(self):
        """Element not an integer"""
        my_list = [1, 2, 5, "three"]
        with self.assertRaises(TypeError):
            max_integer(my_list)
