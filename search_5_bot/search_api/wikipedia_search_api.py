# -*- coding: utf-8 -*-
"""wikipedia_search_api module."""
import wikipedia
import re
import traceback

# local imports
import generic_search_api


class WikipediaSearchApi(generic_search_api.GenericSearchApi):
    """Represent an API to get information from Wikipedia."""

    __base_url = 'https://{}.wikipedia.org/wiki/{}'

    def __init__(self):
        """Instantiate the DuckDuckgo class."""
        pass

    def get_search_results(self, keywords, language):
        """
        Send a HTML request and save results into a list of dictionaries.

        **Args:**

        * keywords - Search terms
        * language - Search language

        **Returns:**

        * List of dictionaries from JSON that contains a title, a description
        and an url
        """
        search_results = list()
        try:
            wikipedia.set_lang(language)
        except Exception as e:
            raise
        else:
            title_results = wikipedia.search(query=keywords, results=5)
            for page_title in title_results:

                new_search_field = dict()

                try:
                    # Try to get the page
                    page_object = wikipedia.page(title=page_title)

                except wikipedia.exceptions.PageError as e:
                    traceback.print_exc(e)
                    raise

                else:

                    # Result title
                    title = page_title
                    new_search_field['title'] = title

                    # Result description
                    description = page_object.summary[:100] + '...'
                    new_search_field['description'] = description

                    # URL
                    title_to_url = re.sub(r'( )', '_', title)
                    url = self.__base_url.format(language, title_to_url)
                    new_search_field['url'] = url

                    search_results.append(new_search_field)

            return search_results
