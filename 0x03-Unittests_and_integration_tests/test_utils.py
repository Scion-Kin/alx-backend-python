#!/usr/bin/python3
''' Defines a test '''

from unittest import TestCase
from utils import access_nested_map as access
from parameterized import parameterized


class TestAccessNestedMap(TestCase):
    """ Defines a test class """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nest, path, output):
        ''' Tests the utils access_nested_map function '''

        self.assertEqual(access(nest, path), output)
