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

    @parameterized.expand([
        ("random-url", {'repos_url': 'http://some_url.com'})
    ])
    def test_public_repos_url(self):
        with patch.object(
                GithubOrgClient, 'org',
                new_callable=PropertyMock
            )
        as mock_org:

    @patch('client.get_json')
    def test_public_repos(self, mocked_method):
        """Testing publi repos """
        payload = [{"name": "Google"}, {"name": "TT"}]
        mocked_method.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_public:

            mocked_public.return_value = "world"
            response = GithubOrgClient('test').public_repos()

            self.assertEqual(response, ["Google", "TT"])

            mocked_public.assert_called_once()
            mocked_method.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """testing license"""
        gh_org_client = GithubOrgClient("google")
        client_has_licence = gh_org_client.has_license(repo, key)
        self.assertEqual(client_has_licence, expected)


if __name__ == '__main__':
    unittest.main()
