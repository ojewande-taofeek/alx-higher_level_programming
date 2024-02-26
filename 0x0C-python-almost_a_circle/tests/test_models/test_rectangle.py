#!/usr/bin/python3
"""The unit tests for rectangle class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
from contextlib import redirect_stdout


class TestRectangle(unittest.TestCase):
    """The test case for the rectangle class"""
    def test_import(self):
        """Test if rectangle is imported"""
        self.assertTrue(Rectangle(10, 2))

    def test_is_instance(self):
        """Test if object is an instance of Rectangle, Base and Object"""
        rec = Rectangle(10, 2)
        self.assertIsInstance(rec, Base)
        self.assertIsInstance(rec, Rectangle)
        self.assertIsInstance(rec, object)
        self.assertTrue(issubclass(type(rec), Rectangle))
        self.assertTrue(issubclass(type(rec), Base))
        self.assertTrue(issubclass(type(rec), object))

    def test_rectangle_attributes(self):
        """Test the attr values of an instance"""
        rec = Rectangle(10, 2, 2, 3, 5)
        self.assertEqual(rec.width, 10)
        self.assertEqual(rec.height, 2)
        self.assertEqual(rec.x, 2)
        self.assertEqual(rec.y, 3)
        self.assertEqual(rec.id, 5)

        rec = Rectangle(10, 2)
        self.assertEqual(rec.width, 10)
        self.assertEqual(rec.height, 2)
        self.assertEqual(rec.x, 0)
        self.assertEqual(rec.y, 0)
        self.assertEqual(rec.id, 8)

    def test_rectangle_exceptions(self):
        """Test for attr values exceptions"""
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle("10", 2)
        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(10, [2])
        with self.assertRaises(TypeError, msg="x must be an integer"):
            Rectangle(10, 2, (5,))
        with self.assertRaises(TypeError, msg="y must be an integer"):
            Rectangle(10, 2, 5, "4")
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(-12, 2)
        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(1, 0)
        with self.assertRaises(ValueError, msg="height must be > 0"):
            Rectangle(1, -4)
        with self.assertRaises(ValueError, msg="x must be >= 0"):
            Rectangle(1, 3, -4)
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            Rectangle(1, 3, 4, -7)

    def test_area(self):
        """Test the value for area"""
        rec = Rectangle(10, 2)
        self.assertEqual(rec.area(), 20)

    def test_display(self):
        """Test the display method"""
        rec_dis = Rectangle(2, 3)
        expected_output = "##\n##\n##"
        with StringIO() as buffer, redirect_stdout(buffer):
            rec_dis.display()
            buf_out = buffer.getvalue().strip()
            self.assertEqual(buf_out, expected_output)

        rec_dis2 = Rectangle(2, 2, 2, 2, 5)
        expected_output = "\n\n  ##\n  ##\n"
        with StringIO() as buffer, redirect_stdout(buffer):
            rec_dis2.display()
            buf_out = buffer.getvalue()
            self.assertEqual(buf_out, expected_output)

    def test_str(self):
        """Test the informal string representation a rectangle object"""
        rec_str = Rectangle(12, 3, 4, 7, 9)
        expected_output = "[Rectangle] (9) 4/7 - 12/3"
        with StringIO() as buffer, redirect_stdout(buffer):
            print(rec_str)
            output = buffer.getvalue().strip()
            self.assertEqual(expected_output, output)

    def test_update(self):
        """Test the update method"""
        rec_up = Rectangle(12, 3, 4, 7, 9)
        rec_up.update(15)
        expected_output = "[Rectangle] (15) 4/7 - 12/3"
        with StringIO() as buffer, redirect_stdout(buffer):
            print(rec_up)
            output = buffer.getvalue().strip()
            self.assertEqual(expected_output, output)

        rec_up.update(15, 2)
        expected_output = "[Rectangle] (15) 4/7 - 2/3"
        with StringIO() as buffer, redirect_stdout(buffer):
            print(rec_up)
            output = buffer.getvalue().strip()
            self.assertEqual(expected_output, output)

        rec_up.update(15, 2, 5)
        expected_output = "[Rectangle] (15) 4/7 - 2/5"
        with StringIO() as buffer, redirect_stdout(buffer):
            print(rec_up)
            output = buffer.getvalue().strip()
            self.assertEqual(expected_output, output)

        rec_up.update(15, 2, 5, 10)
        expected_output = "[Rectangle] (15) 10/7 - 2/5"
        with StringIO() as buffer, redirect_stdout(buffer):
            print(rec_up)
            output = buffer.getvalue().strip()
            self.assertEqual(expected_output, output)

        rec_up.update(15, 2, 5, 10, 71)
        expected_output = "[Rectangle] (15) 10/71 - 2/5"
        with StringIO() as buffer, redirect_stdout(buffer):
            print(rec_up)
            output = buffer.getvalue().strip()
            self.assertEqual(expected_output, output)

        rec_up.update(15, 2, 5, 10, 71, 68)
        expected_output = "[Rectangle] (15) 10/71 - 2/5"
        with StringIO() as buffer, redirect_stdout(buffer):
            print(rec_up)
            output = buffer.getvalue().strip()
            self.assertEqual(expected_output, output)

        rec_up.update()
        expected_output = "[Rectangle] (15) 10/71 - 2/5"
        with StringIO() as buffer, redirect_stdout(buffer):
            print(rec_up)
            output = buffer.getvalue().strip()
            self.assertEqual(expected_output, output)

    def test_update_kwargs(self):
        """Test the update method for keyworded arguments"""
        r1 = Rectangle(10, 10, 10, 10, 12)

        r1.update(height=2)
        expected_output = "[Rectangle] (12) 10/10 - 10/2"
        with StringIO() as buffer, redirect_stdout(buffer):
            print(r1)
            output = buffer.getvalue().strip()
            self.assertEqual(expected_output, output)

        r1.update(3, 2, id=14)
        expected_output = "[Rectangle] (3) 10/10 - 2/2"
        with StringIO() as buffer, redirect_stdout(buffer):
            print(r1)
            output = buffer.getvalue().strip()
            self.assertEqual(expected_output, output)

        r1.update(height=2, x=5)
        expected_output = "[Rectangle] (3) 5/10 - 2/2"
        with StringIO() as buffer, redirect_stdout(buffer):
            print(r1)
            output = buffer.getvalue().strip()
            self.assertEqual(expected_output, output)

    def test_dictionary(self):
        """Test the to_dictionary method"""
        rec = Rectangle(2, 3, 7, 9, 21)
        expected = {'id': 21, 'width': 2, 'height': 3, 'x': 7, 'y': 9}
        output = rec.to_dictionary()
        self.assertDictEqual(expected, output)

        self.assertTrue(issubclass(type(output), dict))
