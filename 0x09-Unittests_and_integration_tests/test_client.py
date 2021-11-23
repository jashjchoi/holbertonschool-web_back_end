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
        test = GithubOrgClient(org_name)
        test.org()
        url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(url)
