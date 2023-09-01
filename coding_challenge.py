import requests
import unittest

"""
== General ==
The objective of this exercise is to create automated tests to validate some basic functionalities of
Discogs' artists search mechanism.
  
The search function required credential. We use the basic key/secret in this case to simplify the
process. The key/secret values are provided in the test class setup function.
  
Search endpoint documentation API:
    https://www.discogs.com/developers#page:database,header:database-search
 
 
== Test Framework ==
 
The test will use the Python's unit test framework
 
Python unit Test :
    https://docs.python.org/3/library/unittest.html
 
== Tests Objectives ==
 
Add the tests for the following :
- Proof that search will fail only when having a incorrectly define Authorization header
- Proof that search pagination will operate based on specs. You may use artist filtering (or other filtering option like using a type) to reduce the resultset to parse.


== IMPORTANT ==

A key/secret pair will be share upon request to do the challenge.

Otherwise it's possible to get a personnal one upon registering with Discogs.

"""

key = "TO_BE_PROVIDED"
secret = "TO_BE_PROVIDED"
discog_url = "https://api.discogs.com/database"


class Discogs:
    """ Class wrapper to interface with Discogs API
    """

    def __init__(self, base_url, key, secret):

        self.base_url = base_url
        self.key = key
        self.secret = secret

        self._set_headers()

    def _set_headers(self):
        auth = f"Discogs key={self.key}, secret={self.secret}"
        self.headers = {
            "Authorization": auth
            }

    def search(self):
        res = requests.get(f"{self.base_url}/search", headers=self.headers)

        print(res.request)
        print(res.json())

        return res


class TestSecurityDiscogs(unittest.TestCase):

    def validate_auth_response(res, expeted_status):
        """
        Function to validate result
        """
        pass

    def test_add_here(self):
        pass


class TestSearchDiscogs(unittest.TestCase):

    def validate_search_response(res, expeted_status, expected_record_nbr):
        """
        Function to validate reseult
        """

        pass

    def test_add_here(self):
        pass


if __name__ == '__main__':
    unittest.main()
