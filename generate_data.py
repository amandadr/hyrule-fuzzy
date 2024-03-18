import requests
import csv
import random

"""
Use this to generate a dataset of misspelled words for fuzzy_search in misspelled_words.csv
"""

# API URL
api_url = "https://botw-compendium.herokuapp.com/api/v3/compendium/"

# CONSTANTS
NUM_VARIATIONS = 50

def introduce_misspelling(word, NUM_VARIATIONS):
    misspelled_words = []
    for _ in range(NUM_VARIATIONS):
        # Combining multiple misspelling techniques
        misspelled = word
        for _ in range(3):  # Apply {num} operations
            operation = random.choice(['swap', 'replace', 'omit', 'add-space', 'remove-space', 'add', 'repeat'])
            
            if operation == 'swap':
                if len(misspelled) > 1:
                    i, j = random.sample(range(len(misspelled)), 2)
                    misspelled = misspelled[:i] + misspelled[j] + misspelled[i+1:j] + misspelled[i] + misspelled[j+1:]
            elif operation == 'replace':
                if len(misspelled) > 1:
                    index = random.randint(0, len(misspelled)-1)
                    new_char = random.choice('abcdefghijklmnopqrstuvwxyz')
                    misspelled = misspelled[:index] + new_char + misspelled[index+1:]
            elif operation == 'omit':
                if len(misspelled) > 1:
                    index = random.randint(0, len(misspelled)-1)
                    misspelled = misspelled[:index] + misspelled[index+1:]
            elif operation == 'add-space':
                if len(misspelled) > 1:
                    index = random.randint(0, len(misspelled))
                    misspelled = misspelled[:index] + ' ' + misspelled[index:]
            elif operation == 'remove-space':
                if len(misspelled) > 1:
                    if ' ' in misspelled:
                        index = random.randint(0, len(misspelled))
                        misspelled = misspelled[:index] + misspelled[index+1:]
            elif operation == 'add':
                if len(misspelled) > 1:
                    index = random.randint(0, len(misspelled))
                    new_char = random.choice('abcdefghijklmnopqrstuvwxyz')
                    misspelled = misspelled[:index] + new_char + misspelled[index:]
            elif operation == 'repeat':
                if len(misspelled) > 1:
                    index = random.randint(0, len(misspelled)-1)
                    misspelled = misspelled[:index] + misspelled[index]*2 + misspelled[index+1:]
        misspelled_words.append(misspelled)
    return misspelled_words

def generate_misspelled_dataset(api_url, NUM_VARIATIONS, filename="misspelled_words.csv"):
    response = requests.get(api_url)
    data = response.json()
    
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['correct', 'misspelled']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for entry in data['data']:
          name = entry['name']

          # Generate multiple misspellings
          misspellings = introduce_misspelling(name, NUM_VARIATIONS)
          for misspelled_name in misspellings[:NUM_VARIATIONS]:
              if misspelled_name != name:
                  writer.writerow({'correct': name, 'misspelled': misspelled_name})


# Run the function to generate the dataset
generate_misspelled_dataset(api_url, NUM_VARIATIONS)
print(f"Dataset containing {NUM_VARIATIONS} misspellings per item saved to 'misspelled_words.csv'")