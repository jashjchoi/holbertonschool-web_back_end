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

class TestGetJson(unittest.TestCase):
    """Unit test for utils.get_json
    """
    @parameterized.expand([
         ("http://example.com", {"payload": True}),
         ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """test that utils.get_json returns the expected result
        """
        test_mock = Mock()
        test_mock.json.return_value = test_payload

        with patch('requests.get', return_value=test_mock):
            res = get_json(test_url)
            self.assertEqual(res, test_payload)
            test_mock.json.assert_called_once()
