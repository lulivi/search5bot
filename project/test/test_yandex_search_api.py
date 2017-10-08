#!/usr/bin/env python
"""Test batery for yandex_api_search module."""

######################################
# test/test_yandex_search_api.py
######################################

# === Test yandex search api ===

# external imports
import unittest
import json
import requests

# path imports
import __init__

# internal imports
from yandex_search_api import YandexSearchApi


class TestYandexSearchApi(unittest.TestCase):
    """Testing class for module yandex."""

    def test_get_search_resutls(self):
        """Test if the results are correct."""
        search_item = 'iphone'
        self.assertFalse(
            YandexSearchApi.search_results(search_item)[1] == [],
            'Not empty list')
