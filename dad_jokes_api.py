import requests

DAD_JOKE_API_URL = 'https://icanhazdadjoke.com/'
DAD_JOKE_SEARCH_URL = f'{DAD_JOKE_API_URL}/search'

def main():
    jokes = search_dad_jokes('dog')
    pass

def search_dad_jokes(search_term, page=1, limit=20):

    # Clean the search term
    search_term = str(search_term).strip().lower()

    # Setup the query string parameters
    query_params = {
        'page': page,
        'limit': limit,
        'term': search_term
    }

    # Setup the header parameters
    header_params = {
        'Accept': 'application/json'
    }

    # Send a GET request for dad jokes that contain search term
    print(f'Searching for dad jokes containing "{search_term}"...', end='')
    resp_msg = requests.get(DAD_JOKE_SEARCH_URL, params=query_params, headers=header_params)

    # Check whether the request was successful
    if resp_msg.ok:
        print('success')
        body_dict = resp_msg.json()
        jokes_portion = body_dict['results']
        jokes_list = [j['joke'] for j in jokes_portion]
        return jokes_list
    else:
        print("failure")
        print(f"Response code: {resp_msg.status_code} ({resp_msg.reason})")
        print(f"Error: {resp_msg.text}")

def get_random_dad_joke():
    # Setup the header parameters
    header_params = {
        'Accept': 'application/json'
    }

    # Send a GET request for a random dad joke
    print('Getting a random dad joke...', end='')
    resp_msg = requests.get(DAD_JOKE_API_URL, headers=header_params)

    # Check whether the request was successful
    if resp_msg.ok:
        print('success')
        body_dict = resp_msg.json()
        return body_dict['joke']
    else:
        print("failure")
        print(f"Response code: {resp_msg.status_code} ({resp_msg.reason})")
        print(f"Error: {resp_msg.text}")

if __name__ == "__main__":
    main()