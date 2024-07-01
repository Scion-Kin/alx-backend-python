#!/usr/bin/env python3
''' Defines a test case '''

from parameterized import parameterized
from unittest import TestCase
from unittest.mock import Mock, patch
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


class TestGetJson(TestCase):
    ''' Defines a test case '''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        ''' Tests the get_json function from utils '''

        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as get:
            self.assertEqual(get_json(test_url), test_payload)
            get.assert_called_once_with(test_url)
