

class DuckDuckGoApiSearch:

    __URL_TO_CALL = http://api.duckduckgo.com/?q=@TERM_TO_SEARCH@&format=json

    def search(term_to_search):
        """
        Return a list of results from DuckDuckGoApi

        **Args:**

        *term_to_search - The term to search

        **Returns*

        *List of results obtained by the API
        """
