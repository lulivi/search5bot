#!/usr/bin/env python
"""Test batery for yandex_api_search module."""

######################################
# test/test_yandex_search_api.py
######################################

# === Test yandex search api ===

# external imports
import unittest

# path imports
import __init__ as test_init

# internal imports
from yandex_search_api import YandexSearchApi


class TestYandexSearchApi(unittest.TestCase):
    """Testing class for module yandex."""

    def test_get_search_resutls(self):
        """Test if the results are correct."""
        search_item = 'iphone'
        yandex_sa = YandexSearchApi(YANDEX_API_USER, YANDEX_API_KEY)
        self.assertFalse(
            yandex_sa.get_search_result(search_item) == [],
            'Not empty list')
