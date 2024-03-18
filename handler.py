import json
import fuzzy_search

"""
Use this handler to have the Lambda function return matches in an HTML response format
"""

def search_handler(event, context):
    search_term = event['search_term'] if 'search_term' in event else event['queryStringParameters']['search_term']
    matches = fuzzy_search.find_fuzzy_matches(search_term)
    return {
        'statusCode': 200,
        'body': json.dumps(matches)
    }