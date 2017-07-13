#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_reg(self):
        self.assertEqual(max_integer([2,4,6,8,10]), 10)

    def test_none(self):
        self.assertIsNone(max_integer([None]))

    def test_empty(self):
        self.assertIsNone(max_integer([]))

    @unittest.expectedFailure
    def string_first(self):
        self.assertEqual(max_integer(["test", 4, 6, 8]), "broken")

    def test_bool_set(self):
        self.assertEqual(max_integer([1, 3, True, 2]), 3)

    @unittest.expectedFailure
    def test_float(self):
        self.assertEqual(max_integer([1.2, 2, 3]), "broken")

    def test_negatives(self):
        self.assertEqual(max_integer([-2, -4, -139]), -2)

    @unittest.expectedFailure
    def test_single_arg(self):
        self.assertEqual(max_integer(1), "broken")

    @unittest.expectedFailure
    def test_None_alone(self):
        self.assertEqual(max_integer(None), "broken")

    @unittest.expectedFailure
    def test_string_alone(self):
        self.assertEqual(max_integer("Holberton"), "broken")

    @unittest.expectedFailure
    def test_bool_alone(self):
        self.assertEqual(max_integer(True), "broken")

    def test_huge_num(self):
        self.assertEqual(max_integer([3819389389183918, 3, 2]), 3819389389183918)

    @unittest.expectedFailure
    def test_many_Nones(self):
        self.assertEqual(max_integer([None, None, 2]), "broken")

    def test_nothing(self):
        self.assertIsNone(max_integer())

    def test_many_spaces(self):
        self.assertIsNone(max_integer(    ))

    @unittest.expectedFailure
    def test_crazy_chars(self):
        self.assertEqual(max_integer("@&^@&"), "broken")

    def test_bools_only(self):
        self.assertEqual(max_integer([True, True, False]), 1)
