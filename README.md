# General
The objective of this exercise is to create automated tests to validate some basic functionalities of
Discogs' artists search mechanism.
  
The search function required credential. We use the basic key/secret in this case to simplify the
process. The key/secret values are provided in the test class setup function.
  
Search endpoint documentation API:
    https://www.discogs.com/developers#page:database,header:database-search
 
 
## Test Framework
 
The test will use the Python's unit test framework
 
Python unit Test :
    https://docs.python.org/3/library/unittest.html
 
## Tests Objectives
 
As per the search API specs, we want to cover the following basic tests cases.
 
Add the tests for the following :
- Proof that search will fail only when having a incorrectly define Authorization header
- Proof that search pagination will operate based on specs. You may use artist filtering (or other filtering option like using a type) to reduce the resultset to parse.

# IMPORTANT

A key/secret pair will be share upon request to do the challenge.

Otherwise it's possible to get a personnal one upon registering with Discogs.
