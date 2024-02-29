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

    def test_to_json_string(self):
        """Test the to_json_string method"""
        json_string = Base.to_json_string([])
        self.assertEqual("[]", json_string)

        json_string = Base.to_json_string(None)
        self.assertEqual("[]", json_string)

        rec = Rectangle(4, 2, 7, 1, 89)
        dictionary = rec.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        expected = '[{"id": 89, "width": 4, "height": 2, "x": 7, "y": 1}]'
        self.assertEqual(json_string, expected)

        squ = Square(4, 7, 1, 89)
        dictionary = squ.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        expected = '[{"size": 4, "id": 89, "x": 7, "y": 1}]'
        self.assertEqual(json_string, expected)

    def test_from_json_string(self):
        """Test the from_json_string() method"""
        json_obj = Base.from_json_string("[]")
        self.assertEqual(json_obj, [])

        json_obj = Base.from_json_string(None)
        self.assertEqual(json_obj, [])

        json_obj = Base.from_json_string('[{"id": 121}]')
        self.assertEqual(json_obj, [{"id": 121}])

        json_obj = Base.from_json_string('[{"id": 121, "width": 21}]')
        self.assertEqual(json_obj, [{"id": 121, "width": 21}])
    """
    def test_save_to_file(self):
        Test for saving a list_objts to file
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r", encoding="utf-8") as file:
            val = file.read()
        self.assertEqual(val, "[]")

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r", encoding="utf-8") as file:
            val = file.read()
        self.assertEqual(val, "[]")

        Square.save_to_file([])
        with open("Square.json", "r", encoding="utf-8") as file:
            val = file.read()
        self.assertEqual(val, "[]")

        Square.save_to_file(None)
        with open("Square.json", "r", encoding="utf-8") as file:
            val = file.read()
        self.assertEqual(val, "[]")

        Base.save_to_file(None)
        with open("Base.json", "r", encoding="utf-8") as file:
            val = file.read()
        self.assertEqual(val, "[]")

        Base.save_to_file([])
        with open("Base.json", "r", encoding="utf-8") as file:
            val = file.read()
        self.assertEqual(val, "[]")

        rec1 = Rectangle(2, 3, 7, 4, 43)
        rec = Rectangle.save_to_file([rec1])
        expected = [{'id': 43, 'width': 2, 'height': 3, 'x': 7, 'y': 4}]
        with open("Rectangle.json", "r", encoding="utf-8") as file:
            val = file.read()
        inst_val = json.loads(val)
        self.assertListEqual(expected, inst_val)

        rec1 = Rectangle(2, 3, 7, 4, 43)
        rec2 = Rectangle(2, 3, 7, 4, 45)
        rec = Rectangle.save_to_file([rec1, rec2])
        expected = [{'id': 43, 'width': 2, 'height': 3, 'x': 7, 'y': 4},
                    {'id': 45, 'width': 2, 'height': 3, 'x': 7, 'y': 4}]
        with open("Rectangle.json", "r", encoding="utf-8") as file:
            val = file.read()
        inst_val = json.loads(val)
        self.assertListEqual(expected, inst_val)
        """
