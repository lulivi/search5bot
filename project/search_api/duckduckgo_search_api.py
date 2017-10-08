# === DuckDuckGo search api ===
"""yandex_api_search module."""

# external imports
import requests
import lxml.html
import re

from urllib import parse

# internal imports
import generic_search_api


class DuckDuckGoSearchApi(generic_search_api.GenericSearchApi):
    """Represent an API to get information from Yandex Search API."""

    _ROOT_URL = 'https://duckduckgo.com/html/?q='

    def __init__(self):
        """Instantiate the Yandex API."""
        pass

    def get_search_results(self, keywords):
        """
        Send a HTML request and save results into a list of dictionaries.

        **Args:**

        * keywords - Search terms

        **Returns:**

        * List of dictionaries from JSON that contains a title, a description
        and an url
        """
        search_results = []
        if keywords != '':
            html_page = requests.get(self._ROOT_URL + keywords)
            html_tree = lxml.html.fromstring(html_page.content)
            # list with every search result
            html_search_results = html_tree.find_class("web-result")

            for search_result in html_search_results:

                new_search_field = dict()

                # Result title
                title_tag = search_result.find_class('result__title')[0]
                title = title_tag.find_class('result__a')[0].text_content()
                new_search_field['title'] = title

                # Result description
                description_tag = search_result.find_class('result__snippet')[
                    0]
                description = description_tag.text_content()
                new_search_field['description'] = description

                # Result URL
                url_tag = search_result.find_class('result__url')[0]
                dirty_url = parse.unquote(url_tag.attrib['href'])
                url = re.search(r'http.*', dirty_url).group()
                new_search_field['url'] = url

                search_results.append(new_search_field)

        return search_results


if __name__ == '__main__':
    ddg = DuckDuckGoSearchApi()
    search_results = ddg.get_search_results("hola")

    print(search_results)
