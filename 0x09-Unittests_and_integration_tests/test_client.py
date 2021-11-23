#!/usr/bin/env python3
"""TestClient module"""

import unittest
from parameterized import parameterized
from utils import requests, get_json
from unittest.mock import Mock, patch
import client
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Unit test for GithubOrgClient class
    @parameterized.expand as a decorator to parametrize the test
    with a couple of org examples to pass to GithubOrgClient
    """
    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": True}),
    ])
    def test_org(self, org, test_payload):
        """GitHubOrgClient.org
        """
        with patch('client.get_json', return_value=test_payload) as test_mock:
            github_test = GithubOrgClient(org_name=org)
            res = github_test.org
            self.assertEqual(res, test_payload)
            test_mock.assert_called_once()
