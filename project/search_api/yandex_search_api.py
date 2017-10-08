# === Yandex search api ===
"""yandex_api_search module."""

# external imports
import yandex_search
import os

# internal imports
import generic_search_api


class YandexSearchApi(generic_search_api.GenericSearchApi):
    """Represent an API to get information from Yandex Search API."""

    __yandex = None
    _YANDEX_API_USER = os.getenv('YANDEX_API_USER')
    _YANDEX_API_KEY = os.getenv('YANDEX_API_KEY')

    def __init__(self):
        """
        Instantiate the Yandex API.

        **Args:**

        * api_user - Yandex API username
        * api_key - Yandex API key
        """
        self.__yandex = yandex_search.Yandex(
            api_user=self._YANDEX_API_USER, api_key=self._YANDEX_API_KEY)

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


if __name__ == '__main__':
    yan = YandexSearchApi()
    print(yan.get_search_result("hola"))
