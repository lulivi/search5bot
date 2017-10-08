#!/usr/bin/env python
"""Test batery for duckduckgo_api_search module."""

# === Test duckduckgo search api ===

# external imports
import unittest

# path imports
import __init__ as init

# internal imports
from duckduckgo_search_api import DuckDuckGoSearchApi


class TestYandexSearchApi(unittest.TestCase):
    """Testing class for module yandex."""

    def test_get_search_resutls(self):
        """Test if the results are correct."""
        search_item = 'hola'
        ddg_sa = DuckDuckGoSearchApi()
        self.assertFalse(
            ddg_sa.get_search_results(search_item) == [], 'Not empty list')
