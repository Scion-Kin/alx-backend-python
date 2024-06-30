#!/usr/bin/python3
''' Defines a test '''

from unittest import TestCase
from utils import access_nested_map as access


class TestAccessNestedMap(TestCase):
    """ Defines a test class """

    @parameterized.expand
    def test_access_nested_map(self):
        ''' Tests the utils access_nested_map function '''

        self.assertEqual(access(nested_map={"a": 1}, path=("a",)), 1)
        self.assertEqual(access(nested_map={"a": {"b": 2}}, path=("a",)),
                         {"b": 2})
        self.assertEqual(access(nested_map={"a": {"b": 2}}, path=("a", "b")),
                         2)
