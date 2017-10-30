# -*- coding: utf-8 -*-
"""wikipedia_search_api module."""
import re
import json
import requests
from urllib.parse import unquote_plus as unquote_url

# local imports
import generic_search_api


class WikipediaSearchApi(generic_search_api.GenericSearchApi):
    """Represent an API to get information from Wikipedia."""

    def __init__(self):
        """Instantiate the WikipediaSearchApi class."""
        self.__actual_language = ''
        self.__actual_url = 'https://{}.wikipedia.org/w/api.php'
        self.__base_url = 'https://{}.wikipedia.org/w/api.php'
        pass

    def _set_lang(self, language):
        """
        Set the language for the next search.

        Sets the current language and insert the language in the base url to
        get the actual url

        Args:

        * language - search langauge
        """
        self.__actual_language = language
        self.__actual_url = self.__base_url.format(language)

    def get_search_results(self, keywords, language):
        """
        Get a search from wikipedia.

        Performs a request to search for a page called `keywords` with
        underscores.

        Args:

        * keywords - Search terms
        * language - Search language

        Returns:

        * List of dictionaries from JSON that contain a title, a description
        and an url
        """
        # Set api language
        if self.__actual_language != language:
            self._set_lang(language)

        # Get the keywords with underscores instead of spaces for the url
        search_keyword = re.sub(r'( )', '_', keywords)

        params = dict(

            # The opensearch protocol
            action='opensearch',

            # Our actuals search keywords
            search=search_keyword,

            # 5 + 1 because the first item in desambiguation is the
            # desambiguation itself
            limit='6',

            # Namespace of articles
            namespace='0',

            # Format of the request
            format='json')

        # Perform the main request
        response = requests.get(url=self.__actual_url, params=params)

        # Create a list for the entries
        search_results = list()

        # No errors
        if response.ok:

            # Load the content of the request into a dictionary
            content = json.loads(response.content)

            # Valid url page
            if content[2] != []:

                # Existent url page
                if content[2][0] != '':

                    # Article page
                    if len(content[1]) == 1:

                        new_search_field = dict()

                        # Title
                        title = content[1][0]
                        new_search_field['title'] = title

                        # Description
                        description = content[2][0]
                        new_search_field['description'] = description

                        # URL
                        url = content[3][0]
                        new_search_field['url'] = unquote_url(url)

                        search_results.append(new_search_field)

                    # Desambiguation page
                    else:

                        # From the second item because the first one is the
                        # desambiguation itself
                        for actual_item in range(1, len(content[1])):

                            new_search_field = dict()

                            # Title
                            title = content[1][actual_item]
                            new_search_field['title'] = title

                            # Description
                            description = content[2][actual_item]
                            new_search_field['description'] = description

                            # URL
                            url = content[3][actual_item]
                            new_search_field['url'] = unquote_url(url)

                            search_results.append(new_search_field)

                # Redirect url page
                else:
                    pass

            # Non valid url page
            else:
                pass

        # Page not existent
        else:
            pass

        return search_results
