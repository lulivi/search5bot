#!/usr/bin/env python
"""Test batery for wikipedia_api_search module."""

######################################
# test/test_wikipedia_search_api.py
######################################

# === Test wikipedia search api ===

# external imports
import unittest

# path imports
import __init__ as path_appends

# internal imports
from wikipedia_search_api import WikipediaSearchApi


assert path_appends


class TestYandexSearchApi(unittest.TestCase):
    """Testing class for module yandex."""

    def test_get_search_resutls(self):
        """Test if the results are correct."""
        search_item = 'hola'
        wikipedia_sa = WikipediaSearchApi()
        self.assertFalse(
            wikipedia_sa.get_search_results(search_item) == [],
            'Not empty list')
