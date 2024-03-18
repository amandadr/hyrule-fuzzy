import pandas as pd
from fuzzywuzzy import fuzz

"""
Use this to find fuzzy matches for a search term - MAKE SURE misspelled_words.csv exists! (Run generate_data.py)
"""

def find_fuzzy_matches(search_term, df=pd.read_csv("misspelled_words.csv").values, threshold=65):
    # Find potential matches for the search term
    matches = []
    for correct_name, misspelling in df:
      # Look for exact matches first
      if search_term == correct_name:
        if correct_name not in [match[0] for match in matches]:
          matches.append([correct_name, 100])
        break
      # Look for substring matches second
      for word in correct_name.split():
        if search_term == word:
          if correct_name not in [match[0] for match in matches]:
            matches.append([correct_name, 99])
          break
      # Look for fuzzy matches last
      ratio = fuzz.token_sort_ratio(search_term, correct_name)
      if ratio >= threshold:
        if correct_name not in [match[0] for match in matches]:
          matches.append([correct_name, ratio])
    # Sort according to descending ratio score
    matches = sorted(matches, key=lambda x: -x[1])
    # Remove ratio score from list
    matches = [match[0] for match in matches]

    return matches