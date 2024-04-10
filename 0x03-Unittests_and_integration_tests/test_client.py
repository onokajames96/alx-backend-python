#!/usr/bin/env python3
"""Class GithubOrgClient"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test class for GithubOrgClient.
    """
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, name, mock_get_json):
        """Test org method of GithubOrgClient. """
        client = GithubOrgClient(name)
        expected_url = f'https://api.github.com/orgs/{name}'
        self.assertEqual(client.org, {'name': 'Test'})
        mock_get_json.assert_called_once_with(expected_url)


if __name__ == '__main__':
    unittest.main()
