######################################
# test/test_yandex_search_api.py
######################################

#!/usr/bin/env python

# === Test yandex search api ===
"""
Test batery for yandex_api_search module
"""

# external imports
import unittest
import json
imoprt requests

# path imports
import __init__

# internal imports
import yandex_search_api

from yandex_search_api import yandexSearchApi


class TestYandexSearchApi(unittest.TestCase):
    """Testing class for module yandex."""

    def test_get_search_resutls(self):
        """Tests if the results are correct."""
        yandex_s_a = yandex_search_api.FaroSearchApi()
        url = 'http://www.yandex.com/api?q=iphone&start=1&length=10&l=en&src=web&f=json'
        self.assertFalse(yandex_s_a.search_results(url)[1] == [], 'Not empty list')
        self.assertTrue(yandex_s_a.search_results(url)[0] == 200, 'OK code')
