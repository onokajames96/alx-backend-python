#!/usr/bin/env python3
"""
Testing Utils
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch
from utils import access_nested_map, get_json
import requests


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


class TestGetJson(unittest.TestCase):
    """Unit test for get json module"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Defining the Function for test_get_json"""
        with patch('requests.get') as mock_request:
            mock_request.return_value.json.return_value = test_payload
            self.assertEqual(get_json(url=test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """Test class"""
     def test_memoize(self):
         """ Defining test memoise function"""
         class TestClass:

             def a_method(self):
                 """Method"""
                 return 42

             @memoize
             def a_property(self):
                 """Property """
                 return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()
