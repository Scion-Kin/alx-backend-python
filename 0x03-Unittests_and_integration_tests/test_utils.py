#!/usr/bin/env python3
''' Defines a test case '''

from parameterized import parameterized
from unittest import TestCase
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """ Defines a test class """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nest, path, output):
        ''' Tests the utils access_nested_map function '''

        self.assertEqual(access_nested_map(nest, path), output)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nest, path, exception):
        ''' Tests the utils access_nested_map function '''

        with self.assertRaises(exception):
            access_nested_map(nest, path)
