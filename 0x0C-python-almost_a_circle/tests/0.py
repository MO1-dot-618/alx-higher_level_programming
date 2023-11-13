#!/usr/bin/python3
""" unit tests for class Base """

import unittest
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
