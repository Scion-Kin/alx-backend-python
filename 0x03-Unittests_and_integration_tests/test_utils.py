#!/usr/bin/python3
''' Defines a test case '''

from parameterized import parameterized
from typing import Mapping, Sequence, Union, Dict
from unittest import TestCase
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """ Defines a test class """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nest: Mapping,
                               path: Sequence,
                               output: Union[Dict, int]) -> None:
        ''' Tests the utils access_nested_map function '''

        self.assertEqual(access_nested_map(nest, path), output)
