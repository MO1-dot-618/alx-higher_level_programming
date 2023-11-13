#!/usr/bin/python3
""" unit tests for class Base """

import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ unittests for class Base """

    def test1(self):
        b1 = Base(None)
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test2(self):
        self.assertEqual(12, Base(12).id)

    def test3(self):
        b1 = Base()
        b2 = Base(23)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test4(self):
        """ test if id is public """
        b = Base(23)
        b.id = 15
        self.assertEqual(15, b.id)

class TestRectangle_init(unittest.TestCase):
    """ unittests for class Rectangle initialisation """

    def test_rectangle_inhirit_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(7, Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 2)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 1)

class Test_Rectangle_methods(unittest.TestCase):
    """ test methods __str__ , display, area """

    def test_area(self):
        r = Rectangle(10, 12, 0, 0, 0)
        self.assertEqual(120, r.area())

    def test_area_one_arg(self):
        r = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)

    def test_str(self):
        r = Rectangle(4, 6)
        correct = "[Rectangle] ({}) 0/0 - 4/6".format(r.id)
        self.assertEqual(correct, str(r))

    def capture_printed(r):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        return(captured_output.getvalue())

    def test_display(self):
        r = Rectangle(2, 4, 3, 2, 0)
        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(display, Test_Rectangle_methods.capture_printed(r))
