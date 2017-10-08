# === Faroo search api ===
"""faroo_api_search module."""


import __init__

# external imports
import json
import requests

# internal imports
import generic_search_api


class FarooSearchApi(generic_search_api.GenericSearchApi):
    """Represent an API to get information from Faroo Search API."""

    def get_search_result(url):
        """
        Send a JSON request and save it in a list of dictionaries.

        **Args:**

        * url - JSON page format url

        **Returns:**

        * List of dictionarys from JSON
        * Request status code
        """
        search_results = []
        search_status_code = -1
        if url != '':
            req = requests.get(url)
            search_results = req.json()['results']
            search_status_code = req.status_code
        return (search_results, search_status_code)
