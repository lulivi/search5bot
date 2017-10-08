# === Yandex search api ===
"""yandex_api_search module."""


import __init__ as init

# external imports
import json
import requests
import yandex_search

# internal imports
import generic_search_api


class YandexSearchApi(generic_search_api.GenericSearchApi):
    """Represent an API to get information from Yandex Search API."""

    __yandex = ""

    def __init__(self, api_user, api_key):
        """
        Instantiate the Yandex API.

        **Args:**

        * api_user - Yandex API username
        * api_key - Yandex API key
        """
        self.__yandex = yandex_search.Yandex(
            api_user=api_user,
            api_key=api_key)

    def get_search_result(self, keywords):
        """
        Send a JSON request and save it in a list of dictionaries.

        **Args:**

        * keywords - JSON page format url

        **Returns:**

        * List of dictionaries from JSON that contains a title, an url and
          a description
        """
        search_results = []
        if keywords != '':
            raw_search_results = self.__yandex.search(keywords).items

            for search_result in search_results:
                newSearchField = dict()
                newSearchField['title'] = raw_search_results['title']
                newSearchField['url'] = raw_search_results['url']
                newSearchField['description'] = raw_search_results['snippet']
                search_results.append(newSearchField)

        return search_results
