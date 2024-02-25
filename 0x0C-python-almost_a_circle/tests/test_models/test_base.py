#!/usr/bin/python3
"""Unit tests for the base.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json


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
        self.assertEqual(b.id, 2)
        c = Base(6)
        self.assertEqual(c.id, 6)

    def test_json_to_dict(self):
        """Test the json_to_dictionary method"""
        rec = Rectangle(10, 7, 2, 8, 28)
        rec_dict = rec.to_dictionary()
        rec_dict_list = [rec_dict]
        rec_list = Base.to_json_string(rec_dict_list)
        rec_list_back = json.loads(rec_list)
        self.assertListEqual(rec_dict_list, rec_list_back)

        rec_dict_list = None
        rec_list = Base.to_json_string(rec_dict_list)
        self.assertEqual(rec_list, "[]")

        rec_dict_list = []
        rec_list = Base.to_json_string(rec_dict_list)
        self.assertEqual(rec_list, "[]")

        self.assertTrue(issubclass(type(rec_list), str))
