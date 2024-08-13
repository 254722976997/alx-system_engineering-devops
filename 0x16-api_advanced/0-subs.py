#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    # Define the API URL with the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # Make the request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the response status code is 200 (OK)
    if response.status_code == 200:
        data = response.json()
        # Return the number of subscribers
        return data.get('data', {}).get('subscribers', 0)
    else:
        # Return 0 for invalid subreddit or other issues
        return 0
