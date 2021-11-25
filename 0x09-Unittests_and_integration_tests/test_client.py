#!/usr/bin/env python3
"""TestClient module"""

import unittest
from parameterized import parameterized
from utils import requests, get_json
from unittest.mock import Mock, patch, PropertyMock
import client
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Unit test for GithubOrgClient class
    @parameterized.expand as a decorator to parametrize the test
    with a couple of org examples to pass to GithubOrgClient
    """
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """GitHubOrgClient.org
        """
        test_org = GithubOrgClient(org_name)
        test_org.org()
        url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(url)

    def test_public_repos_url(self):
        """unittest for GithubOrgClient._public_repos_url
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_test:
            payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
            mock_test.return_value = payload
            test_github = GithubOrgClient("google")
            self.assertEqual(test_github._public_repos_url,
                             mock_test.return_value["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mocked_method):
        '''self descriptive'''
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
        ({"license": {"key": "other_license"}}, "my_license", False)])
    def test_has_license(self, x, y, z):
        """Parameterize test_has_license.
        """
        git_c = GithubOrgClient("google")
        res = git_c.has_license(x, y)
        self.assertEqual(res, z)


if __name__ == '__main__':
    unittest.main()
