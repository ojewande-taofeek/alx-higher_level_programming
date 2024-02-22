#!/usr/bin/python3
"""Unit tests for the base.py"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """The test case for Base class"""

    def test_import(self):
        """To test if the class is imported"""
        self.assertTrue(Base())

    def test_create_instance(self):
        """Create an instance of Base"""
        b = Base()
        self.assertIsInstance(b, Base)
        self.assertEqual(type(b), Base)
        self.assertTrue(issubclass(Base, object))

    def test_id(self):
        """Test if id is None if a value is given"""
        b = Base()
        self.assertEqual(b.id, 1)
        c = Base(6)
        self.assertEqual(c.id, 6)
