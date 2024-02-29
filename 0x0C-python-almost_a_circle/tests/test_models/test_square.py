#!/usr/bin/python3
"""The unit tests for Square class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
from contextlib import redirect_stdout
import json


class TestSquare(unittest.TestCase):
    """Unit tests for Square"""

    def test_import(self):
        """Test if Rectangle class is imported"""
        squ = Square(4)
        self.assertTrue(isinstance(squ, Square))
        self.assertTrue(issubclass(type(squ), Square))
        self.assertTrue(issubclass(type(squ), Rectangle))
        self.assertTrue(issubclass(type(squ), Base))
        self.assertTrue(issubclass(type(squ), object))

    def test_attributes(self):
        """Test the various attrs of an object of Square"""
        squ = Square(5)
        self.assertEqual(squ.width, 5)
        self.assertEqual(squ.height, 5)
        self.assertEqual(squ.x, 0)
        self.assertEqual(squ.y, 0)
        self.assertEqual(squ.id, 26)

        squ = Square(5, 3, 4, 23)
        self.assertEqual(squ.width, 5)
        self.assertEqual(squ.height, 5)
        self.assertEqual(squ.x, 3)
        self.assertEqual(squ.y, 4)
        self.assertEqual(squ.id, 23)
        self.assertEqual(squ.area(), 25)

    def test_exception_raise(self):
        """Test for exceptions raised"""
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Square(-5, 2, 4, 17)
        with self.assertRaises(ValueError, msg="x must be > 0"):
            Square(5, -2, 4, 17)
        with self.assertRaises(ValueError, msg="y must be > 0"):
            Square(5, 2, -4, 17)
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Square(0, 2, 4, 17)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Square("0", 2, 4, 17)
        with self.assertRaises(ValueError, msg="x must be an integer"):
            Square(0, [2], 4, 17)
        with self.assertRaises(ValueError, msg="y must be an integer"):
            Square(0, 2, {4}, 17)

    def test_str(self):
        """Test the informal representation of Square"""
        squ = Square(5, 3, 4, 23)
        expected_out = "[Square] (23) 3/4 - 5"

        with StringIO() as buffer, redirect_stdout(buffer):
            print(squ)
            output = buffer.getvalue().strip()
            self.assertEqual(expected_out, output)

    def test_display(self):
        """Test the display method for Square"""
        squ = Square(2, 3, 4, 23)
        expected_output = "\n\n\n\n   ##\n   ##\n"

        with StringIO() as buffer, redirect_stdout(buffer):
            squ.display()
            output = buffer.getvalue()
            self.assertEqual(expected_output, output)

    def test_update(self):
        """Test the update method for Square"""
        squ = Square(3, 7, 2, 12)

        squ.update(8)
        expected = "[Square] (8) 7/2 - 3"
        with StringIO() as buffer, redirect_stdout(buffer):
            print(squ)
            output = buffer.getvalue().strip()
            self.assertEqual(expected, output)

        squ.update(8, 23, 14, 10)
        expected = "[Square] (8) 14/10 - 23"
        with StringIO() as buffer, redirect_stdout(buffer):
            print(squ)
            output = buffer.getvalue().strip()
            self.assertEqual(expected, output)

        squ.update(8, 23, 14, 10, 48)
        expected = "[Square] (8) 14/10 - 23"
        with StringIO() as buffer, redirect_stdout(buffer):
            print(squ)
            output = buffer.getvalue().strip()
            self.assertEqual(expected, output)

        squ.update(size=15)
        expected = "[Square] (8) 14/10 - 15"
        with StringIO() as buffer, redirect_stdout(buffer):
            print(squ)
            output = buffer.getvalue().strip()
            self.assertEqual(expected, output)

        squ.update(size=13, x=7)
        expected = "[Square] (8) 7/10 - 13"
        with StringIO() as buffer, redirect_stdout(buffer):
            print(squ)
            output = buffer.getvalue().strip()
            self.assertEqual(expected, output)

        squ.update(8, 23, id=7, y=1)
        expected = "[Square] (8) 7/1 - 23"
        with StringIO() as buffer, redirect_stdout(buffer):
            print(squ)
            output = buffer.getvalue().strip()
            self.assertEqual(expected, output)

    def test_dictionary(self):
        """Test the to_dictionary method"""
        rec = Square(2, 3, 7, 21)
        expected = {'id': 21, 'size': 2, 'x': 3, 'y': 7}
        output = rec.to_dictionary()
        self.assertDictEqual(expected, output)

        self.assertTrue(issubclass(type(output), dict))

    def test_save_to_file(self):
        """Test for saving a list_objts to file"""
        Square.save_to_file([])
        with open("Square.json", "r", encoding="utf-8") as file:
            val = file.read()
        self.assertEqual(val, "[]")

        Square.save_to_file(None)
        with open("Square.json", "r", encoding="utf-8") as file:
            val = file.read()
        self.assertEqual(val, "[]")

        Square.save_to_file([Square(1, 2, 3, 78)])
        expected = [{'size': 1, 'id': 78, 'x': 2, 'y': 3}]
        with open("Square.json", "r", encoding="utf-8") as file:
            val = file.read()
        inst_val = json.loads(val)
        self.assertListEqual(expected, inst_val)

    def test_create(self):
        """Test the create() method"""
        rec = Square.create(**{"id": 73})
        self.assertTrue(isinstance(rec, Square))

        rec = Square.create(**{"id": 73, "size": 32})
        self.assertTrue(isinstance(rec, Square))

        rec = Square.create(**{"id": 73, "size": 32, "x": 4})
        self.assertTrue(isinstance(rec, Square))

        rec = Square.create(**{"id": 73, "size": 32, "x": 4, "y": 7})
        self.assertTrue(isinstance(rec, Square))
