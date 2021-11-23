#!/usr/bin/env python3
"""Unit test for utils.py"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, requests, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """unit test for utils.access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test utils.access_nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",)),
                           ({"a": 1}, ("a", "b"))])

    def test_access_nested_map_exception(self, nested_map, path):
        """Test access nested map exception
        test that a KeyError is raised for the following inputs:
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
