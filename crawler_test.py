import requests
import urllib.parse

key_words = '李白'
url = 'https://www.baidu.com/s?wd=' + urllib.parse.quote_plus(key_words)

try:
    # Make the GET request
    response = requests.get(url, timeout=10)  # Set a timeout for the request
    # Raise an HTTPError if the HTTP request returned an unsuccessful status code
    response.raise_for_status()
    # Print the contents of the page
    print(response.text)

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')  # Handle HTTP errors
except Timeout as timeout_err:
    print(f'Timeout error occurred: {timeout_err}')  # Handle request timeout
except RequestException as req_err:
    print(f'Request error occurred: {req_err}')  # Handle other requests exceptions

except Exception as err:
    print(f'An error occurred: {err}')  # Handle any other exceptions
