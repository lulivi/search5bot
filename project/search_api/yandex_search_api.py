# === Yandex search api ===
"""yandex_api_search module."""


# external imports
import yandex_search

# internal imports
import __init__ as init
import generic_search_api

from __init__ import YANDEX_API_USER
from __init__ import YANDEX_API_KEY


class YandexSearchApi(generic_search_api.GenericSearchApi):
    """Represent an API to get information from Yandex Search API."""

    __yandex = None

    def __init__(self, api_user, api_key):
        """
        Instantiate the Yandex API.

        **Args:**

        * api_user - Yandex API username
        * api_key - Yandex API key
        """
        self.__yandex = yandex_search.Yandex(
            api_user=YANDEX_API_USER, api_key=YANDEX_API_KEY)

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
