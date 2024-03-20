import requests

"""
Use this to test the Lambda fuzzy search serverless endpoint
"""
url = "https://bpkb9up1mj.execute-api.us-east-1.amazonaws.com/fuzzy-search"

# GET data from fuzzy_search endpoint
def get_fuzzy_search(search_term):
    print(f"Getting fuzzy search for {search_term}...")
    response = requests.get(url, params={'search_term': search_term})
    if response.status_code != 200:
      print(f"{response.status_code}: {response.reason}; check Cloudwatch logs for more information.")
      return
    else:
      return response.json()
  
# Test the function
search_term = "sword"
potential_matches = get_fuzzy_search(search_term)
print(potential_matches)