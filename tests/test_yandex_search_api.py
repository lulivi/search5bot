#!/usr/bin/env python
"""Test batery for yandex_api_search module."""

######################################
# test/test_yandex_search_api.py
######################################

# === Test yandex search api ===

# external imports
import unittest

# path imports
import __init__ as path_appends

# internal imports
import settings
from yandex_search_api import YandexSearchApi


assert path_appends


class TestYandexSearchApi(unittest.TestCase):
    """Testing class for module yandex."""

    def test_get_search_resutls(self):
        """Test if the results are correct."""
        search_item = 'hola'
        yandex_sa = YandexSearchApi(settings.YANDEX_API_USER,
                                    settings.YANDEX_API_KEY)
        self.assertFalse(
            yandex_sa.get_search_results(search_item) == [], 'Not empty list')


if __name__ == '__main__':
    unittest.main()
