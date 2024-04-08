#!/usr/bin/env python3
"""
Testing Utils
"""
from parameterized import parameterized
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ Class for testing Access Nested Map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        """method returns what it is supposed to."""
        self.assertEqual(access_nested_map(nested_map, path), expected_output)

    @parameterized.expand([
        ({}, ("a,"), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, message):
        """
        Test case to verify that KeyError is raised with the expected message.
        """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)

        self.assertEqual(f"KeyError('{message}')", repr(e.exception))
